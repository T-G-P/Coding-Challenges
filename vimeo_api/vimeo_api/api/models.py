from ..extensions import db
from hashlib import sha256, md5
import datetime
import os


class File(db.Model):

    __tablename__ = 'file'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255))
    filehash = db.Column(db.String(128))
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime,
                           default=datetime.datetime.utcnow)
    gone = db.Column(db.Enum('True', 'False', name='gone'),
                     default='False')

    @staticmethod
    def add_file(filename, password=None):
        new_file = File(filename=filename)

        if password:
            new_file._set_password(password)

        new_file._set_filehash(filename)

        db.session.add(new_file)
        db.session.commit()
        return new_file

    @classmethod
    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hash = sha256()
        # Make sure password is a str because we cannot hash unicode objects
        hash.update((password + salt).encode('utf-8'))
        hash = hash.hexdigest()

        password = salt + hash

        return password

    @classmethod
    def _hash_filename(cls, filename):

        hash = md5()
        hash.update(filename.encode('utf-8'))
        hash = hash.hexdigest()
        return hash

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self.password = self._hash_password(password)
        db.session.commit()

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hash = sha256()
        hash.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hash.hexdigest()

    def _set_filehash(self, filename):
        self.filehash = self._hash_filename(filename)
        db.session.commit()

    def _get_filehash(self):
        """Return the hashed version of the password."""
        return self._filehash

    def __repr__(self):
        return '<File ID%r>' % self.id
