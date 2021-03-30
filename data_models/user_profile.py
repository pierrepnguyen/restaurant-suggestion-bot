# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List


class UserProfile:
    def __init__(
        self, name: str = None, companies_to_review: List[str] = None
    ):
        self.name: str = name
        self.companies_to_review: List[str] = companies_to_review
