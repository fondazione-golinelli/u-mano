from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId

from dacite import Optional

from umano import settings
from umano.hal.db import database


@dataclass(repr=True)
class HalData:
    collection_name = None

    _id: Optional[ObjectId]
    create_time: datetime  # date and time of birth
    likes: int
    score: float

    @classmethod
    def get_collection(cls):
        return database[cls.collection_name]

    @property
    def collection(self):
        return self.get_collection()

    @property
    def _cls(self):
        return self.__class__.__name__

    @property
    def classname(self):
        return self._cls

    @property
    def pk(self):
        return self._id is not None and str(self._id) or None

    def to_dict(self):
        d = self.__dict__
        d.update(dict(
            _cls=self._cls
        ))
        if self._id is None:
            d.pop("_id", None)
        return d

    def save(self):
        if not self._id:
            result = self.collection.insert_one(self.to_dict())
            self._id = result.inserted_id
        else:
            self.collection.update({"_id": self._id}, self.to_dict())

    def delete(self):
        if not self._id:
            return
        self.collection.delete_one({"_id": self._id})


@dataclass
class TestData(HalData):
    collection_name = settings.HAL_DATA_TEST_COLLECTION


@dataclass
class AdamsHandCalibration(HalData):
    collection_name = settings.HAL_DATA_ADAMSHAND_COLLECTION


@dataclass
class AdamsHandSession(AdamsHandCalibration):
    collection_name = settings.HAL_DATA_ADAMSHAND_COLLECTION
    duration: float


@dataclass
class ARData(HalData):
    collection_name = settings.HAL_DATA_AR_COLLECTION


@dataclass
class Artwork(ARData):
    title: str
    author: str


@dataclass
class ArtworkInformation(ARData):
    artwork: str
    url: str


@dataclass
class ARSession(ARData):
    duration: str
    device: str


@dataclass
class ARMarkerRecognition(ARData):
    marker: str
    session: str


@dataclass
class ARItinerary(ARData):
    coordinates: list


@dataclass
class ARCoordinate(ARData):
    longitude: float
    latitude: float


@dataclass
class ARInteraction(ARData):
    widget: str
    artwork: str
    session: str  # ref


@dataclass
class OneHandData(HalData):
    collection_name = settings.HAL_DATA_ONEHAND_COLLECTION


@dataclass
class OneHandTouch(HalData):
    collection_name = settings.HAL_DATA_ONEHAND_TOUCH_COLLECTION
    session_id: str
    status: bool


@dataclass
class OneHandPicture(HalData):
    collection_name = settings.HAL_DATA_ONEHAND_PICTURES_COLLECTION
    touch_session_id: str
    src: str
    filename: str
    hand: bool
    image_points: list


@dataclass
class OneHandFeatures(HalData):
    collection_name = settings.HAL_DATA_ONEHAND_FEATURES_COLLECTION
    uid: str
    touch_session_id: str
    image_points: list
    width: Optional[int]
    height: Optional[int]


@dataclass
class OneHandSound(OneHandData):
    features: str  # ref
    src: str  # wav uri


@dataclass
class OneHandFailure(OneHandData):
    pass


@dataclass
class MachineData(HalData):
    """ a computer, like me """
    collection_name = settings.HAL_DATA_MACHINES_COLLECTION
    name: str


@dataclass
class MachineFailure(HalData):
    """ a computer, like me """
    collection_name = settings.HAL_DATA_MACHINES_COLLECTION
    name: str


@dataclass
class ServiceData(HalData):
    collection_name = settings.HAL_DATA_SERVICES_COLLECTION
    host: str  # the machine name
    ip: str
    name: str
    description: str


@dataclass
class ServiceStatus(ServiceData):
    collection_name = settings.HAL_DATA_SERVICES_STATUS_COLLECTION
    status: str


@dataclass
class ServiceStreamingData(ServiceData):
    collection_name = settings.HAL_DATA_SERVICES_STREAMING_COLLECTION
    url: str


@dataclass
class ServiceStart(ServiceData):
    pass


@dataclass
class ServiceRestart(ServiceData):
    pass


@dataclass
class ServiceFailure(ServiceData):
    pass


@dataclass
class ServicePerformance(ServiceData):
    up_time: float
    operations: int


@dataclass
class SoftwareException(HalData):
    collection_name = settings.HAL_DATA_SOFTWARE_COLLECTION
    src: str
    line: str


@dataclass
class SourceCodeFile(HalData):
    collection_name = settings.HAL_DATA_SOFTWARE_COLLECTION
    src: str


@dataclass
class QueryWebResult(HalData):
    collection_name = settings.HAL_DATA_QUERY_WEB_COLLECTION
    query: str
    url: str
    text: str


@dataclass
class QueryImageResult(HalData):
    collection_name = settings.HAL_DATA_QUERY_IMAGE_COLLECTION
    query: str
    url: str
    src: Optional[str]
