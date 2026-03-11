# Copyright The Volcano Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Async HTTP session utilities for AgentCube SDK."""

import aiohttp


def create_async_session(
    connector_limit: int = 100,
    connector_limit_per_host: int = 10,
) -> aiohttp.ClientSession:
    """Create an aiohttp ClientSession with connection pooling.

    Args:
        connector_limit: Total number of simultaneous connections (default: 100).
        connector_limit_per_host: Max connections per host (default: 10).

    Returns:
        A configured aiohttp.ClientSession with a TCPConnector.
    """
    connector = aiohttp.TCPConnector(
        limit=connector_limit,
        limit_per_host=connector_limit_per_host,
    )
    return aiohttp.ClientSession(connector=connector)
