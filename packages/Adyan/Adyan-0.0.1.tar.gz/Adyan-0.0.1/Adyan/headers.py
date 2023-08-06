#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 14:50
# @Author  : Adyan
# @File    : headers.py


from faker import Faker

fake = Faker()


class Headers:

    def headers(self, referer=None, mobile_headers=None):
        while True:
            user_agent = fake.chrome(
                version_from=63, version_to=80, build_from=999, build_to=3500
            )
            if "Android" in user_agent or "CriOS" in user_agent:
                if mobile_headers:
                    break
                continue
            else:
                break
        if referer:
            return {
                "user-agent": user_agent,
                "referer": referer,
            }
        return {
            "user-agent": user_agent,
        }
