import argparse
import datetime
import json
import os
import os.path
import logging
from typing_extensions import Required

DEFAULT_CONFIG_FILE = os.path.join(
    os.environ["HOME"], "config", "idoc.conf"
)

logging.basicConfig(level=logging.INFO)

class IDOCConfiguration(object):
    '''
    Handles the idoc configuration parameters
    Data are stored in and retrieved from a JSON configuration file
    '''

    _settings = {

        'default_class': {
            'board': "ArduinoDummy",
            'camera': "OpenCVCamera",
            'drawer': "DefaultDrawer",
            'result_writer': "CSVResultWriter",
            'roi_builder': "IDOCROIBuilder",
            'tracker': "AdaptiveBGModel"
        },

        'core' : {
            'debug': True
        },

        'network': {

            'port': 9000
        },

        'folders' : {
            'results' : {'path' : '', 'description' : 'Where data will be saved by the saver class.'},
            'paradigms' : {'path' : '', 'description' : 'Directory with paradigm .csv files'},
            'mappings' : {'path' : '', 'description' : 'Directory with mapping .csv files'},
        },

        'users' : {
            'admin' : { # pylint: disable=bad-continuation
                'id' : 1, 'name' : 'admin', 'fullname' : '', 'PIN' : 9999, 'email' : '',
                'telephone' : '', 'group': '', 'active' : False, 'isAdmin' : True,
                'created' : datetime.datetime.now().timestamp()
            }
        },

        'roi_builder': {
            'args': (),
            'kwargs': {}
        },

        'io': {
            'result_writer': {
                'args': (),
                'kwargs': {
                    'max_n_rows_to_insert': 1,
                }
            },

            'camera': {
                'args': (),
                'kwargs': {
                    'framerate': 20, 'exposure_time': 50000,
                    'resolution': (960, 720),
                    'drop_each': 1,
                    'use_wall_clock': True,
                    'wrap': False
                }
            }
        },

        'controller': {
            'paradigm_path': 'warm_up.csv',
            'arduino_port': "/dev/ttyACM0",
            'pwm': {
            },
        },

        'drawer': {
            'args': (),
            'kwargs': {
                'draw_frames': False,
                'video_out_fourcc': "DIVX",
                'framerate': None # match that of the camera
            },
            'last_drawn_path': "/tmp/last_img.png",
            'last_annot_path': "/tmp/last_img_annot.png",
        },

        'experiment': {
            'adaptation_time': 5,
            "max_duration": 18000,
            "location": None
        }
    }


    def __init__(self, config_file=None):

        if config_file is None:
            config_file = DEFAULT_CONFIG_FILE
        self._config_file = config_file
        self.load()

    @property
    def content(self):
        return self._settings

    @property
    def file_exists(self):

        return os.path.exists(self._config_file)

    def save(self):
        """
        Save settings to default json file
        """

        os.makedirs(os.path.dirname(self._config_file), exist_ok=True)

        try:
            with open(self._config_file, 'w') as json_data_file:
                json.dump(self._settings, json_data_file)

            logging.info('Saved idoc configuration file to %s', self._config_file)

        except Exception as error:
            logging.warning('Problem writing to file % s' % self._config_file)
            raise error

    def load(self):
        '''
        Reads saved configuration folders settings from json configuration file
        If file does not exist, creates default settings
        '''

        if not self.file_exists:
            self.save()

        else:
            try:
                with open(self._config_file, 'r') as filehandle:
                    config = "".join(filehandle.readlines())
                
                if config != "":
                    self._settings.update(json.loads(config))
            except:
                raise ValueError("File %s is not a valid configuration file" % self._config_file)

        return self._settings

def main():

    config = IDOCConfiguration()
    config.save()

if __name__ == "__main__":
    main()