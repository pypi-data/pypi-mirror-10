# Copyright (c) Microsoft Corporation.  All rights reserved.

""" Data collections. """


import pydocumentdb.base as base
import pydocumentdb.documents as documents


class Collection(documents.Resource):

    def __init__(self, documentclient, body):
        super(Collection, self).__init__()
        self._documentclient = documentclient

        self._docs = 'docs/'
        self._sprocs = 'sprocs/'
        self._triggers = 'triggers/'
        self._udfs = 'udfs/'
        self._conflicts = 'conflicts/'
        self.LoadFromBody(body)

    def ReadDocuments(self, feed_options={}):
        return self.QueryDocuments(None, feed_options)

    def QueryDocuments(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._docs
        def result_fn(result):
            return result['Documents']
        def create_fn(parent, body):
            return Document(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'docs',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def CreateDocument(self, body, options={}):
        path = '/' + self.self_line + self._docs
        self._documentclient.Create(body, path, 'docs', self.id, None, options)
 
    def ReadDocument(self, id, options={}):
        path = '/' + self.self_line + self._docs + id
        self._documentclient.Read(path, 'docs', id, None, options)

    def ExecuteTransientProcedure(self, procedure_function):
        documentclient = self._documentclient
        default_headers = documentclient.default_headers
        initial_headers = {
            'accept': 'application/json',
            'content-type': 'application/x-javascript'
        }
        initial_headers = base.Extend(initial_headers, default_headers)
        url_connection = documentclient.url_connection
        path = '/' + self.self_line + 'sprocs'
        headers = base.GetHeaders(documentclient,
                                  initial_headers,
                                  'post',
                                  path,
                                  self.id,
                                  'sprocs',
                                  {})

        return documentclient.Post(url_connection,
                                   path,
                                   procedureFunction,
                                   headers)

    def ReadTriggers(self, options={}):
        return self.QueryTriggers(None, options)

    def QueryTriggers(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._triggers
        def result_fn(result):
            return result['Triggers']
        def create_fn(parent, body):
            return Trigger(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'triggers',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def CreateTrigger(self, trigger, options={}):
        if trigger.server_script:
            trigger.body = str(trigger['server_script'])
        elif trigger.body:
            trigger.body = str(trigger['body'])
           
        path = '/' + self.self_line + self._triggers
        self._documentclient.Create(trigger,
                                    path,
                                    'triggers',
                                    self.id,
                                    None,
                                    options)

    def ReadTrigger(self, id, options={}):
        path = '/' + self.self_line + self._triggers + id
        self._documentclient.Read(path, 'triggers', id, None, options)

    def ReadUserDefinedFunctions(self, option={}):
        return self.QueryUserDefinedFunctions(None, options)

    def QueryUserDefinedFunctions(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self.udfs
        def result_fn(result):
            return result['UserDefinedFunctions']
        def create_fn(parent, body):
            return UserDefinedFunction(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'udfs',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def CreateUserDefinedFunction(self, udf, options={}):
        if udf.server_script:
            udf.body = str(udf['server_script'])
        elif udf.body:
            udf.body = str(udf['body'])

        path = '/' + self.self_line + self._udfs
        self._documentclient.Create(udf,
                                    path,
                                    'udfs',
                                    self.id,
                                    None,
                                    options)

    def ReadUserDefinedFunction(self, id, options={}):
        path = '/' + self.self_line + self._udfs + id
        self._documentclient.Read(path, 'udfs', id, None, options)

    def ReadStoredProcedures(self, options={}):
        return self.QueryStoredProcedures(None, options)

    def QueryStoredProcedures(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._sprocs
        def result_fn(result):
            return result['StoredProcedures']
        def create_fn(parent, body):
            return StoredProcedure(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'sprocs',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)

    def CreateStoredProcedure(self, sproc, options={}):
        if sproc.server_script:
            sproc.body = str(sproc['server_script'])
        elif sproc.body:
            sproc.body = str(sproc['body'])
        path = '/' + self.self_line + self._sprocs
        return self._documentclient.Create(sproc,
                                           path,
                                           'sprocs',
                                           self.id,
                                           None,
                                           options)

    def ReadStoredProcedure(self, id, options={}):
        path = '/' + self.self_line + self._sprocs + id
        self._documentclient.Read(path, 'sprocs', id, None, options)

    def ReadConflicts(self, feed_options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._conflicts
        def result_fn(result):
            return result['Conflicts']
        def create_fn(parent, body):
            return Conflict(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'conflicts',
                                        self.id,
						                result_fn,
						                create_fn,
                                        '',
                                        options)

    def ReadConflict(self, id, options={}):
        path = '/' + self.self_line + self._conflicts + id
        return self._documentclient.Read(path, 'conflicts', id, None, options)

    def Replace(self, collection, options={}):
        path = '/' + self.self_line
        return self._documentclient.Replace(collection,
                                            path,
                                            'colls',
                                            self.id,
                                            None,
                                            options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        return self._documentclient.DeleteResource(path,
                                                   'colls',
                                                   self.id,
                                                   None,
                                                   options)


class Document(documents.Resource):

    def __init__(self, documentclient, body):
        super(Document, self).__init__()
        
        self._documentclient = documentclient
        self._attachments = 'attachments/'
        self.LoadFromBody(body)

    def Replace(self, document, options={}):
        path = '/' + self.self_line
        self._documentclient.Replace(document,
                                     path,
                                     'docs',
                                     self.id,
                                     None,
                                     options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'docs',
                                            self.id,
                                            None,
                                            options)

    def CreateAttachment(self, body, options={}):
        path = '/' + self.self_line + self.attachments
        self._documentclient.Create(body,
                                    path,
                                    'attachments',
                                    self.id,
                                    None,
                                    options)

    def CreateAttachmentAndUploadMedia(self, readable_stream, options={}):
        initial_headers = base.Extend({}, self._documentclient.default_headers)

        # Add required headers slug and content-type.
        if options.slug:
            initial_headers.slug = options.slug

        if options.content_type:
            initial_headers['content-type'] = options.content_type
        else:
            initial_headers['content-type'] = 'application/octet-stream'

        path = '/' + self.self_line + self._attachments
        self._documentclient.Create(readable_stream,
                                    path,
                                    'attachments',
                                    self.id,
                                    initial_headers,
                                    options)

    def ReadAttachment(self, id, options={}):
        path = '/' + self.self_line + self._attachments + id
        self._documentclient.Read(path, 'attachments', id, None, options)

    def ReadAttachments(self, options={}):
        return self.QueryAttachments(none, options)

    def QueryAttachments(self, query, options={}):
        documentclient = self._documentclient
        path = '/' + self.self_line + self._attachments
        def result_fn(result):
            return result['Attachments']
        def create_fn(parent, body):
            return Attachment(documentclient, body)
        return documentclient.QueryFeed(documentclient,
                                        path,
                                        'attachments',
                                        self.id,
                                        result_fn,
                                        create_fn,
                                        query,
                                        options)


class Attachment(documents.Resource):

    def __init__(self, documentclient, body):
        super(Attachment, self).__init__()
        self._documentclient = documentclient
        self.LoadFromBody(body)

    def ReadMedia(self):
        documentclient = self._documentclient
        defaultHeaders = documentclient.default_headers
        url_connection = documentclient.url_connection
        media_id = self.media.split('/')[2]
        path = '/' + self.media
        headers = base.GetHeaders(documentclient,
                                  default_headers,
                                  'get',
                                  path,
                                  media_id,
                                  'media',
                                  {})

        return documentclient.Get(urlConnection, path, headers)

    def UpdateMedia(self, readable_stream, options={}):
        documentclient = self._documentclient
        default_headers = documentclient.default_headers
        initial_headers = base.Extend({}, default_headers)

        # Add required headers slug and content-type in case the body is a stream
        if options.slug:
            initial_headers.slug = options.slug

        if options.content_type:
            initial_headers['content-type'] = options.content_type
        else:
            initial_headers['content-type'] = 'application/octet-stream'

        url_connection = documentclient.url_connection
        media_id = self.media.split('/')[2]
        path = '/' + self.media
        headers = base.GetHeaders(documentclient,
                                  initial_headers,
                                  'put',
                                  path,
                                  media_id,
                                 'media',
                                 options)

        documentclient.Put(url_connection, path, readable_stream, headers)

    def Replace(self, attachment, options={}):
        path = '/' + self.self_line
        self._documentclient.Replace(attachment,
                                    path,
                                    'attachments',
                                    self.id,
                                    None,
                                    options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'attachments',
                                            self.id,
                                            None,
                                            options)


class Trigger(documents.Resource):
    
    def __init__(self, documentclient, body):
        super(Trigger, self).__init__()
        self._documentclient = documentclient
        self.LoadFromBody(body)

    def Replace(self, trigger, options={}):
        if trigger.server_script:
            trigger.body = str(trigger['server_script'])
        elif trigger.body:
            trigger.body = str(trigger['body'])
            
        path = '/' + self.self_line
        self._documentclient.Replace(trigger,
                                    path,
                                    'triggers',
                                    self.id,
                                    None,
                                    options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'triggers',
                                            self.id,
                                            None,
                                            options)


class UserDefinedFunction(documents.Resource):

    def __init__(self, documentclient, body):
        super(UserDefinedFunction, self).__init__()
        self._documentclient = documentclient
        self.LoadFromBody(body)

    def Replace(self, udf, options={}):
        if udf.serverScript:
            udf.body = str(udf['server_script'])
        elif udf.body:
            udf.body = str(udf['body'])

        path = '/' + self.self_line
        self._documentclient.Replace(udf,
                                     path,
                                     'udfs',
                                     self.id,
                                     None,
                                     options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'udfs',
                                            self.id,
                                            None,
                                            options)


class StoredProcedure(documents.Resource):

    def __init__(self, documentclient, body):
        super(StoredProcedure, self).__init__()
        self.__documentclient = documentclient
        self.LoadFromBody(body)

    def Execute(self, params):
        documentclient = self._documentclient
        default_headers = documentclient.default_headers
        initial_headers = {
            'accept': 'application/json'
        }

        initial_headers = base.Extend(initial_headers, default_headers)
        if params and not type(params) is list:
            params = [params]

        url_connection = documentclient.url_connection
        path = '/' + self.self_line
        headers = base.GetHeaders(documentclient,
                                  initial_headers,
                                  'post',
                                  path,
                                  self.id,
                                  'sprocs',
                                  {})

        return documentclient.Post(url_connection, path, params, headers)

    def replace(self, sproc, options={}):
        if sproc.server_script:
            sproc.body = str(sproc['server_script'])
        elif sproc.body:
            sproc.body = str(sproc['body'])

        path = '/' + self.self_line
        self._documentclient.Replace(sproc,
                                     path,
                                     'sprocs',
                                     self.id,
                                     None,
                                     options)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'sprocs',
                                            self.id,
                                            None,
                                            options)


class Conflict(documents.Resource):

    def __init__(self, documentclient, body):
        super(Conflict, self).__init__()
        self._documentclient = documentclient
        self.LoadFromBody(body)

    def Delete(self, options={}):
        path = '/' + self.self_line
        self._documentclient.DeleteResource(path,
                                            'conflicts',
                                            self.id,
                                            None,
                                            options)