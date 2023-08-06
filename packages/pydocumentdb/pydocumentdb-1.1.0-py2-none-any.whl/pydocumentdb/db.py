# Copyright (c) Microsoft Corporation.  All rights reserved.

""" Database class and other related classes. """


import pydocumentdb.base as base
import pydocumentdb.documents as documents


class Database(documents.Resource):
    """ Database model. """

    def __init__(self, documentclient, body):
        super(Database, self).__init__()
        self._documentclient = documentclient
        self._colls = body['colls'] if 'colls' in body else 'colls/'
        self._users = body['users'] if 'users' in body else 'users/'
        self.LoadFromBody(body)

    def ReadCollections(self, options={}):
        return self.QueryCollections(None, options)

    def QueryCollections(self, query, options={}):
        path = '/' + self.self_line + self._colls
        documentclient = self._documentclient
        def result_fn(result):
            return result['DocumentCollections']
        def create_fn(parent, body):
            return Collection(documentclient, body)
        return self.QueryFeed(documentclient,
                              path,
                              'colls',
                              self.id,
                              result_fn,
                              create_fn,
                              query,
                              options)

    def CreateCollection(self, body, options={}):
        path = '/' + self.self_line + self._colls
        return self._documentclient.Create(body,
                                           path,
                                           'colls',
                                           self.id,
                                           None,
                                           options)

    def ReadCollection(self, id, options={}):
        path = '/' + self.self_line + self._colls + id
        return self._documentclient.Read(path, 'colls', id, None, options)

    def CreateUser(self, body, options={}):
        path = '/' + self.self_line + self._users
        return self._documentclient.Create(body,
                                           path,
                                           'users',
                                           self.id,
                                           None,
                                           options)

    def ReadUsers(self, options={}):
        return self.QueryUsers(None, options)

    def ReadUser(self, id, options={}):
        path = '/' + self.self_line + self._users + id
        self._documentclient.Read(path, 'users', id, None, options)

    def QueryUsers(self, query, options={}):
        path = '/' + self.self_line + self._users
        documentclient = self._documentclient
        def result_fn(result):
            return result['Users']
        def create_fn(parent, body):
            return User(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'users',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def Replace(self, db, options={}):
        path = '/' + self.self_line
        return self._documentclient.Replace(db,
                                            path,
                                            'dbs',
                                            self.id,
                                            None,
                                            options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        return self._documentclient.DeleteResource(path,
                                                   'dbs',
                                                   self.id,
                                                   None,
                                                   options)


class User(documents.Resource):

    def __init__(self, documentclient, body):
        super(User, self).__init__()
        self._documentclient = documentclient
        self._permissions = 'permissions/'
        self.LoadFromBody(body)

    def CreatePermission(self, body, options={}):
        path = '/' + self.self_line + self._permissions
        return self._documentclient.Create(body,
                                           path,
                                           'permissions',
                                           self.id,
                                           None,
                                           options)

    def ReadPermission(self, id, options={}):
        path = '/' + self.self_line + self._permissions + id
        self._documentclient.Read(path,
                                  'permissions',
                                  id,
                                  None,
                                  options)
        return self.QueryPermissions(None, options)

    def QueryPermissions(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._permissions
        def result_fn(result):
            return result['Permissions']
        def create_fn(parent, body):
            return Permission(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'permissions',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def Replace(self, user, options={}):
        path = '/' + self.self_line
        self._documentclient.Replace(user,
                                     path,
                                     'users',
                                     self.id,
                                     None,
                                     options)

    def Delete(options={}):
        path = '/' + self.self_line
        return self._documentclient.DeleteResource(path,
                                                   'users',
                                                   self.id,
                                                   None,
                                                   options)


class Permission(documents.Resource):

    def __init__(self, documentclient, body):
        super(Permission, self).__init__()
        self._documentclient = documentclient
        self.LoadFromBody(body)

    def Replace(self, permission, options={}):
        path = '/' + self.self_line
        return self._documentclient.Replace(permission,
                                            path,
                                            'permissions',
                                            self.id,
                                            None,
                                            options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        return self._documentclient.DeleteResource(path,
                                                   'permissions',
                                                   self.id,
                                                   None,
                                                   options)