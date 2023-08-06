############################
### Main callable script
############################

import json
import logging
import logging.handlers
import os
import signal
from threading import Thread
import urllib.parse

import bottle

from idoc.decorators import warning_decorator, error_decorator, wrong_id
from idoc.server.core.control_thread import ControlThread
from idoc.helpers import get_machine_id, get_git_version, get_server
from idoc.configuration import IDOCConfiguration

from .parser import get_parser, list_options

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='IDOC.log',
                    filemode='w')

logger = logging.getLogger('')
logging.getLogger('idoc.server.io.pylon_camera').setLevel(logging.DEBUG)


socket_handler = logging.handlers.SocketHandler(
    'localhost',
    logging.handlers.DEFAULT_TCP_LOGGING_PORT
)

logger.addHandler(socket_handler)


def set_server(host, port):
    app = bottle.Bottle()
    return app, bottle, None

PORT = 9000
app, bottle, server = set_server(host="0.0.0.0", port=PORT)


@app.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root="/")

@app.post("/settings/<id>")
@warning_decorator
@wrong_id
def update():
    r"""
    Receive the new settings passed by the user
    via a POST request in JSON format.
    A partial update is ok i.e. not all parameters
    need to be supplied, only those changing.
    A dictionary with the current values is returned
    upong GETting to this same URL.
    """

    post_data = bottle.request.body.read() # pylint: disable=no-member

    if isinstance(post_data, bytes):
        data_decoded = post_data.decode()
    else:
        data_decoded = post_data

    try:
        data_parsed = json.loads(data_decoded)
    except json.decoder.JSONDecodeError:
        data_parsed = urllib.parse.parse_qs(data_decoded)

    settings = data_parsed['settings']
    submodule = data_parsed['submodule']
    if submodule == "control_thread":
        control_thread.settings = settings
    else:
        target = control
        for module in submodule:
            target = getattr(target, module)

        if target is not None:
            target.settings = settings
        else:
            logger.warning("Module %s is not initialized yet.", module)

    return {"status": "success"}


@app.get("/settings/<id>")
@wrong_id
@warning_decorator
def report():
    r"""
    Return current value of the settings to the user
    Settings can be updated by POSTing to the same URL.
    """
    settings = control_thread.settings
    return settings


@app.get("/info/<id>")
@warning_decorator
@wrong_id
def inform():
    r"""
    Return information about the control thread to the user,
    contained in the info property.
    """
    return control_thread.info

@app.get('/id')
@error_decorator
def get_id():
    r"""
    Return the content of /etc/machine-id to the user.
    URLs are suffixed in the API to check the supplied id
    with the id of the machine.
    A mismatch is interpreted as a user mistake and a
    WrongMachineID expception is raised.
    """
    return {"id": control_thread.info["id"]}


@app.post('/load_paradigm/<id>')
@warning_decorator
@wrong_id
def load_paradigm():
    r"""
    Update the hardware paradigm loaded in IDOC.
    Do this by posting an object with key paradigm_path
    and value the filename of one of the csv files in the
    paradigms_dir.
    paradigms_dir is defined in the config file under
    folders > paradigms > path.
    A list of the paradigms can be retrieved by GETting to /list_paradigms/.
    """
    post_data = bottle.request.body.read() # pylint: disable=no-member
    if isinstance(post_data, bytes):
        data_decoded = post_data.decode()
    else:
        data_decoded = post_data

    try:
        data_parsed = json.loads(data_decoded)
    except json.decoder.JSONDecodeError:
        data_parsed = urllib.parse.parse_qs(data_decoded)

    paradigm_path = data_parsed["paradigm_path"][0]
    control_thread.load_paradigm(paradigm_path=paradigm_path)
    return {"status": "success"}


@app.post('/description/<id>')
@warning_decorator
@wrong_id
def description():
    r"""
    Set a description of the experiment
    """
    post_data = bottle.request.body.read() # pylint: disable=no-member
    if isinstance(post_data, bytes):
        data_decoded = post_data.decode()
    else:
        data_decoded = post_data

    data_parsed = json.loads(data_decoded)
    control_thread.description = data_parsed["description"]

    return {"status": "success"}


@app.get('/list_paradigms/<id>')
@warning_decorator
@wrong_id
def list_paradigms():
    r"""
    Get a list of the available paradigms that the user
    can select via POSTing to /load_paradigm.
    This is also available in info["controller"]["paradigms"].
    """
    return control_thread.list_paradigms()

@app.get('/mapping/<id>')
@warning_decorator
@wrong_id
def mapping():
    r"""
    Tell the user that is the hardware-board pin mapping loaded in IDOC
    This is also available in info["controller"]["mapping"].
    """
    return control_thread.mapping

@app.get('/pin_state/<id>')
@warning_decorator
@wrong_id
def pin_state():
    r"""
    Return the status of the board pins
    This is also available in info["controller"]["pin_state"]
    """
    return control_thread.pin_state


@app.get('/controls/<submodule>/<action>/<id>')
@warning_decorator
@wrong_id
def control(submodule, action):
    r"""
    Command the IDOC modules.
    Set a submodule as ready, start or stop it by supplying
    ready, start and stop as action
    Actions are available for the recognizer and controller modules
    as well as the control thread.
    """
    if submodule == "control_thread" and action == "stop":
        # exit the application completely
        stop()

    return control_thread.command(submodule, action)


@app.post("/controls/toggle/<id>")
@warning_decorator
@wrong_id
def toggle():

    post_data = bottle.request.body.read() # pylint: disable=no-member
    if isinstance(post_data, bytes):
        data_decoded = post_data.decode()
    else:
        data_decoded = post_data

    logger.debug(data_decoded)

    data_parsed = json.loads(data_decoded)
    hardware = data_parsed["hardware"]
    value = float(data_parsed["value"])
    return control_thread.toggle(hardware, value)



@app.get('/choices/<category>/<id>')
@warning_decorator
@wrong_id
def list_choices(category):
    return list_options(category)



def run(port, debug):
    server = get_server(port)
    logger.info("Running bottle on server %s, port %d", server, port)
    bottle.run(app, host='0.0.0.0', port=port, debug=debug, server=server)


def stop(signo=None, _frame=None):
    r"""
    A function to bind the arrival of specific signals to an action.
    """
    logger.debug("Received signal %s", signo)
    try:
        control_thread.stop()
        logger.info('Quitting')
        os._exit(0) # pylint: disable=protected-access
        # sys.exit(0)
    except Exception as error:
        logger.warning(error)

    return


def main(ap=None, args=None):

    if args is None:
        ap = get_parser()
        args = ap.parse_args()

    global control_thread

    config = IDOCConfiguration()
    ARGS = vars(args)

    machine_id = get_machine_id()
    version = get_git_version()
    RESULT_DIR = config.content["folders"]["results"]["path"]
    DEBUG = ARGS.pop("debug") or config.content["network"]["port"]

    if DEBUG:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.info("You have passed arguments:")
    logger.info(ARGS)

    control_thread = ControlThread(
        machine_id=machine_id,
        version=version,
        result_dir=RESULT_DIR,
        user_data=ARGS,
    )
    
    server_thread = Thread(target=run, name="bottle", args=(PORT, DEBUG))

    signals = ('TERM', 'HUP', 'INT')
    for sig in signals:
        signal.signal(getattr(signal, 'SIG' + sig), stop)

    control_thread.start()
    server_thread.start()
    control_thread.join()
    stop()


if __name__ == "__main__":
    main()
