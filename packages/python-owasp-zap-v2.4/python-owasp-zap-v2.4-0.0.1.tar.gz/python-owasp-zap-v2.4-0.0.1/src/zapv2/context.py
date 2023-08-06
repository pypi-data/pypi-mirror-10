# Zed Attack Proxy (ZAP) and its related class files.
#
# ZAP is an HTTP/HTTPS proxy for assessing web application security.
#
# Copyright 2015 the ZAP development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This file was automatically generated.
"""

class context(object):

    def __init__(self, zap):
        self.zap = zap

    @property
    def context_list(self):
        """
        List context names of current session
        """
        return next(self.zap._request(self.zap.base + 'context/view/contextList/').itervalues())

    def exclude_regexs(self, contextname):
        """
        List excluded regexs for context
        """
        return next(self.zap._request(self.zap.base + 'context/view/excludeRegexs/', {'contextName' : contextname}).itervalues())

    def include_regexs(self, contextname):
        """
        List included regexs for context
        """
        return next(self.zap._request(self.zap.base + 'context/view/includeRegexs/', {'contextName' : contextname}).itervalues())

    def context(self, contextname):
        """
        List the information about the named context
        """
        return next(self.zap._request(self.zap.base + 'context/view/context/', {'contextName' : contextname}).itervalues())

    def exclude_from_context(self, contextname, regex, apikey=''):
        """
        Add exclude regex to context
        """
        return next(self.zap._request(self.zap.base + 'context/action/excludeFromContext/', {'contextName' : contextname, 'regex' : regex, 'apikey' : apikey}))

    def include_in_context(self, contextname, regex, apikey=''):
        """
        Add include regex to context
        """
        return next(self.zap._request(self.zap.base + 'context/action/includeInContext/', {'contextName' : contextname, 'regex' : regex, 'apikey' : apikey}))

    def new_context(self, contextname='', apikey=''):
        """
        Creates a new context in the current session
        """
        return next(self.zap._request(self.zap.base + 'context/action/newContext/', {'contextName' : contextname, 'apikey' : apikey}))

    def export_context(self, contextname, contextfile, apikey=''):
        return next(self.zap._request(self.zap.base + 'context/action/exportContext/', {'contextName' : contextname, 'contextFile' : contextfile, 'apikey' : apikey}))

    def import_context(self, contextfile, apikey=''):
        return next(self.zap._request(self.zap.base + 'context/action/importContext/', {'contextFile' : contextfile, 'apikey' : apikey}))

    def set_context_in_scope(self, contextname, booleaninscope, apikey=''):
        """
        Sets a context to in scope (contexts are in scope by default)
        """
        return next(self.zap._request(self.zap.base + 'context/action/setContextInScope/', {'contextName' : contextname, 'booleanInScope' : booleaninscope, 'apikey' : apikey}))


