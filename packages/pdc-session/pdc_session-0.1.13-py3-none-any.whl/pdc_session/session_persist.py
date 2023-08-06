import pickle

from requests import Session

from pdc_session.types.session_exception import ReleaseZero

from .session_config import SessionConfig
from .types.client import Payload
from .api.session import create_session, find_session, lock_session, release_session, update_session
from .helpers.logger import create_logger

logger = create_logger(__name__)

class SessionPersist(SessionConfig):
    
    username: str
    session: Session
    session_id: int
    session_valid: bool
    picks: list = ['username', 'session']

    def __enter__(self):
        self._acquire()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self._release()


    def get_session(self):

        logger.debug('get session')
        data = find_session(self.username)

        if data['error']:

            self.session_valid = False
            logger.error(data['msg'])
            if data['msg'] == 'no session unlock':
                return self.all_locked()
            
            return
        
        byte = bytes(data['data']['session_data'], 'utf-8')
        object = pickle.loads(byte)


        self.__dict__.update(object)
        self.session_id = data['data']['id']
        self.session_valid = True


    def update_session(self) -> bool:

        logger.debug('update session')

        data = {}
        for key, value in self.__dict__.items():
            if key in self.picks:
                data[key] = value

        session_id = self.session_id
        session = pickle.dumps(data, 0).decode('utf-8')

        update = update_session(session_id, session)
        if update['error']:
            logger.error(update['msg'])
            return False
        
        return True


    def lock_session(self):
        
        logger.debug('lock session')

        lock = lock_session(self.session_id)
        if lock['error']:
            logger.error(lock['msg'])
            return False

        return True


    def release_session(self):

        logger.debug('release session')

        if not self.session_id:
            raise ReleaseZero(f'[{self.username}] session 0')

        release = release_session(self.session_id)
        if release['error']:
            logger.error(release['msg'])
            return False

        return True


    def create(self, lock=True):

        logger.debug('create session')
        data = {}
        for key, value in self.__dict__.items():
            if key in self.picks:
                data[key] = value


        session = pickle.dumps(data, 0).decode('utf-8')

        payload: Payload = {
            "username": self.username,
            "session": session
        }
        data = create_session(payload, lock)

        if data['error']:
            logger.error(data['msg'])
            return

        if lock:
            byte = bytes(data['data']['session_data'], 'utf-8')
            sp: SessionPersist = pickle.loads(byte)
            
            self.session_valid = True
            self.session_id = data['data']['id']
            self.session = sp['session']


    def all_locked(self):
        pass


    def _acquire(self):
        # set default
        self.session = Session()
        self.session_id = 0
        self.session_valid = False

        # get session
        self.get_session()
        
        if self.session_valid:
            self.lock_session()


    def _release(self):

        if self.session_valid:
            self.update_session()
            self.release_session()



if __name__ == '__main__':
    class Auth(SessionPersist):

        def __init__(self, username):
            self.username = username

    with Auth('test') as sp:      
        print(sp.api_uri)  
        sp.create()
        print(sp.session.cookies.get_dict())