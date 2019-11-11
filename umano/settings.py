import os

BASE_DIRECTORY = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), "media")
UMANO_SHARE_ROOT = "/umano-share"

HAL_MONGODB_URL = 'mongodb://localhost:27017/'

HAL_BROKER_URL = 'amqp://guest:guest@localhost'
HAL_EXCHANGE_NAME = "umano"

HAL_DATA_ADAMSHAND_COLLECTION = "adam.data"
HAL_DATA_AR_COLLECTION = "ar.data"
HAL_DATA_MACHINES_COLLECTION = "machine.data"
HAL_DATA_ONEHAND_COLLECTION = "onehand"
HAL_DATA_ONEHAND_TOUCH_COLLECTION = "{}.touches".format(HAL_DATA_ONEHAND_COLLECTION)
HAL_DATA_ONEHAND_PICTURES_COLLECTION = "{}.pictures".format(HAL_DATA_ONEHAND_COLLECTION)
HAL_DATA_ONEHAND_FEATURES_COLLECTION = "{}.features".format(HAL_DATA_ONEHAND_COLLECTION)
HAL_DATA_SERVICES_COLLECTION = "services"
HAL_DATA_SERVICES_STATUS_COLLECTION = "{}.status".format(HAL_DATA_SERVICES_COLLECTION)
HAL_DATA_SERVICES_ACKNOWLEDGE_COLLECTION = "{}.ack".format(HAL_DATA_SERVICES_COLLECTION)
HAL_DATA_SERVICES_STREAMING_COLLECTION = "{}.streaming".format(HAL_DATA_SERVICES_COLLECTION)
HAL_DATA_SOFTWARE_COLLECTION = "software.data"
HAL_DATA_TEST_COLLECTION = "test.data"


ONEHAND_MOCKUP_URL = "https://umano.fondazionegolinelli.it/onehand"
ONEHAND_MOCKUP_DOWNLOAD_FOLDER = os.path.join(BASE_DIRECTORY, "downloads")

ONEHAND_MAX_HOST = "127.0.0.1"
ONEHAND_MAX_PORT = 8888
ONEHAND_VUO_HOST = "127.0.0.1"
ONEHAND_VUO_PORT = 8889

ONEHAND_MILLUMIN_HOST = "192.168.109.102"
ONEHAND_MILLUMIN_PORT = 7000

ONEHAND_OSC_BANG_ADDRESS = "/umano/onehand/bang"
ONEHAND_OSC_RECORD_FILENAME_ADDRESS = "/umano/onehand/filename"
ONEHAND_OSC_DURER_FREQ_ADDRESS = "/umano/onehand/durer/freq"
ONEHAND_OSC_DURER_AMP_ADDRESS = "/umano/onehand/durer/amp"
ONEHAND_OSC_HAND_FREQ_ADDRESS = "/umano/onehand/hand/freq"
ONEHAND_OSC_HAND_AMP_ADDRESS = "/umano/onehand/hand/amp"
ONEHAND_OSC_HAND_BEAT_ADDRESS = "/umano/onehand/beat"
ONEHAND_OSC_HAND_ATTACK_ADDRESS = "/umano/onehand/attack"
ONEHAND_OSC_HAND_RELEASE_ADDRESS = "/umano/onehand/release"
ONEHAND_OSC_FINGER_ADDRESS = "/umano/onehand/{}/{}"

ONEHAND_OSC_RANDOM_SEED_ADDRESS = "/umano/cave/random/seed"
ONEHAND_OSC_RANDOM_REPETITION_ADDRESS = "/umano/cave/random/repetition"
ONEHAND_OSC_RANDOM_ENABLE_ADDRESS = "/umano/cave/random/enable"

ONEHAND_HANDPOSE_MODEL_URL = "http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel"

ONEHAND_HAND_PICTURES_FOLDER = os.path.join(MEDIA_ROOT, "onehand/pictures")
ONEHAND_HAND_PICTURES_EXTENSION = ".jpg"
ONEHAND_HAND_AUDIO_FOLDER = os.path.join(MEDIA_ROOT, "onehand/audio")
ONEHAND_HAND_AUDIO_EXTENSION = ".aiff"
ONEHAND_HAND_PRINTS_FOLDER = os.path.join(MEDIA_ROOT, "onehand/handprints")
ONEHAND_HAND_PRINTS_EXTENSION = ".jpg"

ONEHAND_SHARE_FOLDER = os.path.join(UMANO_SHARE_ROOT, "onehand")

ADAM_SERIAL_BAUDRATE = 115200
ADAM_SERIAL_PRESSURE_PORT = "COM4"
ADAM_SERIAL_EGM_PORT = "COM5"
ADAM_SERIAL_EGM_MAX_VALUE = 1023
ADAM_SERIAL_ENCODING = "UTF-8"

ADAM_OSC_RECEIVER_HOST = "127.0.0.1"
ADAM_OSC_RECEIVER_PORT = 8889
ADAM_OSC_PRESSURE_ADDRESS = "/umano/adam/pressure"

CAMERA_STREAM_LIVE_URL = '/video_feed'


try:
    from .local_settings import *
except ImportError:
    print("local settings not found")

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)
if not os.path.exists(ONEHAND_HAND_PICTURES_FOLDER):
    os.makedirs(ONEHAND_HAND_PICTURES_FOLDER)
if not os.path.exists(ONEHAND_HAND_AUDIO_FOLDER):
    os.makedirs(ONEHAND_HAND_AUDIO_FOLDER)
if not os.path.exists(ONEHAND_HAND_PRINTS_FOLDER):
    os.makedirs(ONEHAND_HAND_PRINTS_FOLDER)

if not os.path.exists(ONEHAND_SHARE_FOLDER):
    os.makedirs(ONEHAND_SHARE_FOLDER)
