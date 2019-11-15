# coding = utf-8
"""
@author: zhou
@time:2019/8/1 10:12
@File: config.py
"""

sleep_time = 5  # 延迟时间，建议配置5-10s
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        "Cookie": "SINAGLOBAL=4979979695709.662.1540896279940; SUB=_2AkMrYbTuf8PxqwJRmPkVyG_nb45wwwHEieKdPUU1JRMxHRl-yT83qnI9tRB6AOGaAcavhZVIZBiCoxtgPDNVspj9jtju; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5d4hHnVEbZCn4G2L775Qe1; login_sid_t=766380e3154e7c07289dfa85f4f39e06; cross_origin_proto=SSL; YF-V5-G0=86b4280420ced6d22f1c1e4dc25fe846; _s_tentry=www.google.com; UOR=bbs.51testing.com,widget.weibo.com,www.google.com; Apache=3869600320705.12.1564573721749; ULV=1564573721766:8:3:1:3869600320705.12.1564573721749:1564019682040; Ugrow-G0=d52660735d1ea4ed313e0beb68c05fc5; YF-Page-G0=8438e5756d0e577d90f6ef4db5cfc490|1564573777|1564573714"
    }
day = 100  # 最久抓取的微博时间，60即为只抓取两个月前到现在的微博