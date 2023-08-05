# Copyright (C) 2014 Nippon Telegraph and Telephone Corporation.
# Copyright (C) 2014 YAMAMOTO Takashi <yamamoto at valinux co jp>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# client for ryu.app.ofctl.service

import numbers

from ryu.base import app_manager
import event


def get_datapath(app, dpid):
    """
    Get datapath object by dpid.

    :param app: Client RyuApp instance
    :param dpid: Datapath-id (in integer)

    Returns None on error.
    """
    assert isinstance(dpid, numbers.Integral)
    return app.send_request(event.GetDatapathRequest(dpid=dpid))()


def send_msg(app, msg, reply_cls=None, reply_multi=False):
    """
    Send an OpenFlow message and wait for reply messages.

    :param app: Client RyuApp instance
    :param msg: An OpenFlow controller-to-switch message to send
    :param reply_cls: OpenFlow message class for expected replies.
        None means no replies are expected.  The default is None.
    :param reply_multi: True if multipart replies are expected.
        The default is False.

    If no replies, returns None.
    If reply_multi=False, returns OpenFlow switch-to-controller message.
    If reply_multi=True, returns a list of OpenFlow switch-to-controller
    messages.

    Raise an exception on error.

    Example::

        import ryu.app.ofctl.api as api

        msg = parser.OFPPortDescStatsRequest(datapath=datapath)
        result = api.send_msg(self, msg,
                                    reply_cls=parser.OFPPortDescStatsReply,
                                    reply_multi=True)
    """
    return app.send_request(event.SendMsgRequest(msg=msg,
                                                 reply_cls=reply_cls,
                                                 reply_multi=reply_multi))()


app_manager.require_app('ryu.app.ofctl.service', api_style=True)
