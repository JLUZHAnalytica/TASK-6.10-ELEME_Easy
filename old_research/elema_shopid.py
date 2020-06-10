# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import requests
import json
import time
import random
offset = 1755
shop_id = []
cookie = [
# # '__wpkreporterwid_=b77b8bef-a3e9-4e81-0e9c-d3881756bf5b; ubt_ssid=ilkha8pse5g4122hgc2yqduzjoac8tg8_2020-06-07; perf_ssid=vfgpud8oofkmr1tu3kshxxhl7mlsp8eb_2020-06-07; ut_ubt_ssid=s2v3ocmhyif1hdz7jumojmapmetwqxii_2020-06-07; _utrace=0d037d42d880d2ce1ad34156121443d2_2020-06-07; cna=zA71FgNiM1QCAduISvHVe3Vn; _bl_uid=mskRnb254hzsCd6eb6Lba7jazaIv; _samesite_flag_=true; cookie2=11d02f565b83c7201762d8aa5e4f1d0d; t=fde297ee74be499a3efabdcec2346e8c; _tb_token_=3571b8773ed05; csg=743201f3; t_eleuc4=id4=0%40BA%2FvuHCrrRtQnIoNSBWw%2FAHuUx%2FAlPtUgj0rqg%3D%3D; munb=2206585031598; SID=AwAAAdGrVjee7AAGXADHJjyTl-2kwgQ01Xmz7kswTfKW9jh_GYJGlbOn; USERID=2000034346910; UTUSER=2000034346910; tzyy=d65545cad93b482e7f2d01f93ed0fdd2; x5check_ele=0iRIN6%2FS2bYCE%2By3Uw2WWENIV%2FXNj2%2BVuuUj5CbAXzc%3D; l=eBQDZ7GrQVjo3wQyBO5anurza77t0IdbzsPzaNbMiIncC6bPdu99goRQLsPKNCtRR8XcGZYB4gR2YAetoeP_8PwfkaQE-1IVlgEvBef..; isg=BKOjh-0q-VagoLViWryng4BMMuFNmDfaqki2-dUBaIIRFME2XWkLKy7GDuQatI_S',
# 'cna=Y49GFtWEfF4CAXjtoAYpZ4UH; ut_ubt_ssid=ri43wqitp430ynmw7ycr12a6ryc28y48_2020-06-07; perf_ssid=nhgkt2live1yp6rv3213birjffjpl8xu_2020-06-07; ubt_ssid=a996l76k3x7yh4lhi31geqsv6c9uezk9_2020-06-07; _utrace=045f1125ecf0d66e71878f1ddcffab1c_2020-06-07; t=fd45e273043b13a0b97adea2108dd5d9; munb=2206588865815; UTUSER=2000035559833; UM_distinctid=1728e0243c83be-08846cb067e683-d373666-130980-1728e0243c94ac; __wpkreporterwid_=1b5ffe47-8ebe-4b19-8abf-f54a131397f9; _bl_uid=4qkk6b794Fau0d8gh75LnR6ynjFe; tzyy=f2cd8ab3f5e535aecdd49c1d9aead181; l=eBxTRMXgQVjHZCiOBOfaFurza7yeYIRfguPzaNbMiOCPO4595l5hWZvQ_hLpCnNVn6uJR3ykIQI_B7TLny4eQxv9-ewyFtQqxdLh.; _samesite_flag_=true; cookie2=1e4db1e0ef314829d402bc1ab808d2b1; _tb_token_=eeeeea8de5e1f; csg=e6a2f4b9; t_eleuc4=id4=0%40BA%2FvuHCrrRtQnIcy%2FZ8MJX%2BO%2Bi8DiqztJo5UTg%3D%3D; SID=BQAAAdGraLmZ7AAGoQBgmy8LgB4rCW1sKopyO0BsLy53qqel438GaQpJ; USERID=2000035559833; x5check_ele=6%2Bu09bmvA3%2FbTGcfCfYxq3nPDUNCzwLV54tk8rg2tM8%3D; isg=BKOjlv8h-Vf2x7ViaX_F_SEUMudNmDfaW6DIiNUARoJ5FMI2XWjeKZMFDqS_tI_S',
# '__wpkreporterwid_=9efcffc6-4925-4ce7-b9aa-c9fc8b275211; ubt_ssid=53oy0qppxthkfjn9kyrcpdbph3s8xkfc_2020-06-07; perf_ssid=yzgiyfz5jygi7h4zlcoedijef93qj6to_2020-06-07; ut_ubt_ssid=3hu294gq3gvzepw99djh1mu3ll1sse81_2020-06-07; cna=TEw9F5MHjFACAbcAlS9mwsbH; _bl_uid=q4k7zb7p5w41mI3tUc9q21g58848; _utrace=e621ca025d83c2856119bfe156cc13bb_2020-06-07; _samesite_flag_=true; cookie2=1e04f9f20f61b041325cce7180211fb9; t=5fd46f991d9334896d771c663b4d5d19; _tb_token_=e3bd9eb306373; munb=2206099961085; SID=DAAAAAFGjimC7AAGTAAPAfefQ9npfUKLKhR4H6tPpAoP8ZuZW-D5w6pX; USERID=5478689154; UTUSER=5478689154; csg=087101eb; t_eleuc4=id4=0%40BA%2FvuHCrrRtVrsfR%2Bgp1%2B7YLeQILbyzz1juZWA%3D%3D; x5check_ele=w3B8MdQzDziMj5kBx7DtfKSOWL3Pi5DNhCvaAKxA5j4%3D; tzyy=0044f0f418df7a693cd9b4b6c93d456e; l=eBgpTt_7QVNdvLvpBOfChurza779RIR8muPzaNbMiOCP9kCD5-zPWZvQNlLkCnGVnsGvJ35QyF6TBDYnTPatQxv9-e1Sm1uq3dRC.; isg=BBAQy3d2ek5f6CZLYYK5CrC24V5i2fQjFhP-wwrh3Ws-RbLvsumPs1J3GQulkaz7',
# '__wpkreporterwid_=fb8f959b-a88b-4f04-a667-d78542d36ea2; ubt_ssid=lihd4mr152c09zd4nr4ezn07svc2s4el_2020-06-07; perf_ssid=1naki75ce4jiizbaj4o0s8ra96pymixo_2020-06-07; ut_ubt_ssid=m66qhwshe7iszci0lncadmz1klzsxs89_2020-06-07; isg=BMbGpXrg5AyRl7DpO1rAyxF3FLxIJwrhf4T4xrDu2unEs2fNGLdL8aECj29_AAL5; l=eBaGaXqVQVTh4sD-BO5Bnurza77T1IO48kPzaNbMiInca18RNF1Z_OQDdSdXldtfgt1LhetyLqt1edKek3fRwxDDBti2PHWs3xf..; UTUSER=2000030235796; _bl_uid=mCkXUb8s5kC1Ow840hn5dhOtOLLj; cna=OLw1F7jgXi0CAduEckxT/7Uj; _utrace=ea83ec38d96805d43cf88f13352bcf2a_2020-06-07; t=f7a272da22198520c7e8fa1692cac12f; t_eleuc4=id4=0%40BA%2FvuHCrrRtQkLM1%2BglHNhk1kjPp44xHTOmVig%3D%3D; munb=2206546129689; SID=BAAAAdGrF3yU7AAGxwCd2FvrjJ4a2fm8NKeWpCQ9o233UQl-XDSPYy47; USERID=2000030235796; x5check_ele=emCex6%2By37piI4Y3aanxzD2JeOYKyzGk2aCAvCeP4mo%3D; tzyy=ffa2c38117eeae13b6957d498e48cc11',
# # '__wpkreporterwid_=52a4dd0e-f0e1-45f9-393d-9914d1e2f80d; ubt_ssid=mqmrh8166zjhen0ylww5cu3k9ppdre2l_2020-06-07; perf_ssid=zpq5i8uj861pb5b5mj7t9d1ees1qweyy_2020-06-07; ut_ubt_ssid=blk5zezfz4t1hu1redces0g8j56w11tg_2020-06-07; cna=e9pXF21sJigCAXF2DXOwC4iK; _bl_uid=Utk6wbF644Iremvn5zzt35k66e83; _utrace=28fe3bba1c0ce75484a3e70f9f99d0e3_2020-06-07; _samesite_flag_=true; cookie2=1ff728153cd5d11078d6ad7c7c4874da; t=b86f23f7ee94141c087ef5d6f60ac6b5; _tb_token_=ed355b1388036; csg=09484496; t_eleuc4=id4=0%40BA%2FvuHCrrRtQk0MqN0A8ZvMLx537DUeqNxrjZQ%3D%3D; munb=2206579483915; track_id=1591519662|1007f241d03ec6fad54df7f148fd7ac1b04c216fcbaff38b51|ff7c1e2216e2db4412046bcf836fcbf7; tzyy=9933c52edbe4e66dbe32ecc02f6db1fa; l=eBOWF_cmQVTtCKsKBOfZhurza77TdIRAguPzaNbMiOCP9O1p7-PAWZvK1vT9CnGVh6qyR35QyF69BeYBq3K-nxv96IUUIrkmn; USERID=250178596; UTUSER=250178596; SID=BgAAAAAO6Wwk6gAEAADESBQvhoNvFQ_z4X7LhT-2BKqGEtJaUeTuFH7g; ZDS=1.0|1591535321|4WzGeyaGPgR/8mevH65FmJCmlKeJtZ6izhxGtSCOhLYqRzRfQs0+9OKUyJlgm362; x5check_ele=z%2FkLKjvd5MChJVArFKGNStcUZsDWklcE60x0Gm%2F33ZQ%3D; isg=BLe3SfdkpVKggSHeUZlmrueQRqsBfIveZf65tglk0wTeuNf6EUwbLnXZnh7mUGNWUwbLnXZnh7mUGNWNW',
# # '__wpkreporterwid_=0dcb3725-ef92-41b5-bab8-5a5d8c230460; ubt_ssid=ch0d41pj8fjipmyrydgxri05hlln3bou_2020-06-07; perf_ssid=auetpn0v2jdg9q8zaikdz7s8snosypbc_2020-06-07; ut_ubt_ssid=ii2hmyzl8ma3b4mg47rkd8jjwzglax2i_2020-06-07; cna=l61JF0upQlECAXjrqQDAckij; _bl_uid=thkCFbR15zC2wzi1eisvxXLqjIpt; _utrace=d4ace16e8b42ecdae76c365468556339_2020-06-07; t=f7af8ea49f3ddb5813cf8aaa5ea0b5b7; l=eBSQkUIIQVNdH23KBOfZnurza7799IRVguPzaNbMiOCP965yJuU5WZvKStY2CnGVnstvJ3RILX7QBc8KkPU67xv9-e9bMdFs3dRC.; track_id=1591535414|083fb2dca5b43f61ef2cd8b5cbe2b32bed3d8c574e227e820a|3e4acd45664c1ddf3b3e6483821f9b73; USERID=1000081288890; UTUSER=1000081288890; SID=CQAAAOjZfW666gAEAAD2UeJN9eWPF1ElvyeMwKu1FlxYPMFgcrbR6j-n; ZDS=1.0|1591535414|lYrb2E0xqpk9h20z/SVATblfSqVILqYTQ+rnTZoFWMTGTg+13w+m/Pd8enMhiuhhlF7PU0c24I5fU/HM8FtXUg==; isg=BDU15SqVhyjEIOOUwgttYp8wRLHvsunEtQMvebda1qz7jl6AbgIplQkP3FS4zgF8',
# '__wpkreporterwid_=52a4dd0e-f0e1-45f9-393d-9914d1e2f80d; ubt_ssid=mqmrh8166zjhen0ylww5cu3k9ppdre2l_2020-06-07; perf_ssid=zpq5i8uj861pb5b5mj7t9d1ees1qweyy_2020-06-07; ut_ubt_ssid=blk5zezfz4t1hu1redces0g8j56w11tg_2020-06-07; cna=e9pXF21sJigCAXF2DXOwC4iK; _bl_uid=Utk6wbF644Iremvn5zzt35k66e83; _utrace=28fe3bba1c0ce75484a3e70f9f99d0e3_2020-06-07; _samesite_flag_=true; t=b86f23f7ee94141c087ef5d6f60ac6b5; _tb_token_=ed355b1388036; csg=09484496; t_eleuc4=id4=0%40BA%2FvuHCrrRtQk0MqN0A8ZvMLx537DUeqNxrjZQ%3D%3D; munb=2206579483915; track_id=1591519662|1007f241d03ec6fad54df7f148fd7ac1b04c216fcbaff38b51|ff7c1e2216e2db4412046bcf836fcbf7; tzyy=9933c52edbe4e66dbe32ecc02f6db1fa; l=eBOWF_cmQVTtCnFKBO5Zhurza77t3IOXhsPzaNbMiInca1yA_hL2aNQDdKL98dtjgtfvxeKPOzL1BRn2JxaU-xaVX9zbTF6ZmYvvF; UTUSER=1000081304180; USERID=1000081304180; SID=DAAAAOjZfap06gAEAADblI1acUonvyoD4E4fVl0oUn2fbD0c7KG0nVdU; ZDS=1.0|1591586159|WGdv8IeEintFPiD2CWLtgHsaK6UDGAGRHEzFFBC/xg46mV/w3bE3YYAfFZzUjPyNE/daZ9zyryRxri4iZeBKRQ==; x5check_ele=YbcTUKJkbaNwLZWZBOWNnWt1wD%2FD0trvs82dyrXpHow%3D; isg=BCIimOLyiKCllpR9AZp63SSFc6iEcyaN2NmsVWy7TxVAP8C5VAMTmKO-a13DL54l',
# # '__wpkreporterwid_=e80951cb-950a-4940-19ea-48aef5666ce8; _bl_uid=3tkeFbFv5190kjepdr4Rusqw44mh; ubt_ssid=jz4gpp061kx0y4dstiqswrkcx9pqdjgu_2020-06-07; perf_ssid=a4p56zqra0fbpkyaf3smcx9ywuv3dop0_2020-06-07; ut_ubt_ssid=j68pcza8uezw497fffwyn96uxvvzst50_2020-06-07; cna=nMNjFzr8+mECAW8TJp0pA8s1; _utrace=7b264d3be9d4a1ecf92f0ba0f8fd3661_2020-06-07; l=eBLxBDMmQVTtvNoKBOfwlurza77OvIRRguPzaNbMiOCP_J1B5isfBZvK1086CnGVnsMWJ3RILX7QBvYnNyznQxv9-e9bMdF_HpdC.; track_id=1591530960|45fe7cbd04b8548c99f807ae93c556c4ee6c9fe98092656d62|476f221d898decf946a046695987bcff; USERID=35820790; UTUSER=35820790; SID=CAAAAAACIpT26gAEAAD-ggzpA5Yck4-p1bh0xa87oFiSs0B2CegitIVP; ZDS=1.0|1591530960|FR2zhuIyX/x/coV67QjpLkxj9nke6DdJAN+ILTRcuFH/+Rdvzs+0hwgh8M/VnJoy; x5check_ele=OzRutFPmDXN58OzuKu8eeQ%3D%3D; tzyy=e032a097c3f26fae73ec10d60b620488; isg=BAkJYJy1s2QP9E-QzrIJZe0sGDVjVv2IYS_Dfat-hPAv8isE86YvWNhjMFDEqpXA',
# '__wpkreporterwid_=63de1d56-a67c-428d-a62e-a7f3949c134f; ubt_ssid=388ki362426n24dti8mxxax9kju6lzut_2020-06-07; perf_ssid=92kx6a2humh554xv2v9y33rj4j826smu_2020-06-07; ut_ubt_ssid=p0xa0yxylzcj4hp3czx78fn4qn8ixrmc_2020-06-07; _bl_uid=esk3ObeC460t5brz8qakpvOhgej3; cna=75djF+qC40oCARu7Th6A3UiO; _utrace=0d736d242aa41d58248bdbf73cb2102f_2020-06-07; t=498c09094ad6f23cb79be81574f8039d; t_eleuc4=id4=0%40BA%2FvuHCrrRUkrvmFBsmjR6fET2COSO%2BzEYAnkQ%3D%3D; munb=2208234537927; SID=CQAAAOjZfLpF7AAGnwA3rwe7vDICJ37eVlT_pLSfK6ETXc0SMqPIfGCz; USERID=1000081242693; UTUSER=1000081242693; x5check_ele=WkvW5x4UEdmh4I%2FQbK7Qj%2FIpJqBc%2FrcoqjEpZgpexww%3D; tzyy=4fd7aaaf36818a1a41d5c040e1f28754; l=eBQggVBrQVjUG-D-BOfChurza77TvIRbmuPzaNbMiOCPOx5BoaT5BZvQakY6CnGVnsEyR3ljL4J_BuY_7y4E0xv9-e1Sm1u4pdTh.; isg=BHR0qgnxlnoUUQI3FM6uhh7fRTLmTZg3sPZavg7VAP-CeRTDNl1oxypw_behhdCP',
# '__wpkreporterwid_=6429f269-f07d-4571-086a-beac52d2c25c; ubt_ssid=ungexh95fgnyy7ady20gyb1gunwfnop8_2020-06-08; perf_ssid=ke8gvg3vmxl9vujlscgs1guc0t1yctv5_2020-06-08; ut_ubt_ssid=9eh6gxlwwm41trx2opph4aguxmuvoc5b_2020-06-08; _bl_uid=tskwFb4b588v35s4gyI9xFvun9Rb; cna=VwhcFy3+aGcCAXjmtP6DFaZf; _utrace=979205f1493e050928eea3f394dccb4b_2020-06-08; _samesite_flag_=true; cookie2=118cd77b1f5474e7dad32ef73bdc1c6a; t=91ab915102c124fb4a0f406ef53ba6d6; _tb_token_=7eee6136e675a; csg=c9c07550; t_eleuc4=id4=0%40BA%2FvuHCrrRtQl5AQ0dCtb0IaafE2NwKMdX4kAw%3D%3D; munb=2206532508981; SID=AgAAAOjVdSns7AAGtACbmfvpo8dpGdXmtG_cWcYKcL2RRCCof3FsnWdo; USERID=1000013638124; UTUSER=1000013638124; x5check_ele=OQc2KPqM4kSaYowoYKqDJ4crfPZR9TmXjoclfOb%2B1WM%3D; tzyy=bfdb769c131f7a9baee88638ade49f0f; isg=BD09wnBvP4FAIZvtzKcfKG35TJ832nEstRBEWv-CSBTDNl1oxyrG_AOn4GJwtonk; l=eBOVenFHQVUD9Lm5BOfZhurza7799IRAguPzaNbMiOCPO81k5Z2hWZvQzx8DCnGNh6-BR37cAizQBeYBc_C-nxvOpiV3pyMmn',
# 'ut_ubt_ssid=pmi3o74gwz1x94l0lr4a2919xw7opzx4_2020-06-07; ubt_ssid=7rwaci72apyxlmqt6zfqzpe7x35r9q4f_2020-06-07; cna=5zzeFtMS70ACAXFRkC0qymBk; _utrace=91eb824f72f7ab12047a6d23a3915b9f_2020-06-07; t=ac5fe679e7ba2fa0b567e0dfb802df3c; t_eleuc4=id4=0%40BA%2FvuHCrrRj3bnAc6PLwZlHrIXf9Kmk2DQi0KA%3D%3D; munb=2205013417283; SID=CAAAAABNyb7q7AAGiABosP8MkuRXX8vXl7imgV-nCAve4P7jQu7K-5hw; USERID=1305067242; UTUSER=1305067242; tzyy=97d578b447b48beaedb451613aa1886f; x5check_ele=4XOMpa%2BpYfNlkiK%2Br%2BX5FuAMVvbo5GEfhs1ZxLWwO3o%3D; l=eBak7P0lQVja473hBOfwhurza77OOIRAguPzaNbMiOCPO4fRdOrRWZvQGPTvCnGVh64pJ3lsGOfzBeYBcCYLLNYe6IUUIWkmn; isg=BFdXc-DBxXNpVEH-MbGbY3nB5s2hnCv-cXjXB6mEXiaj2HcasG-VTD32PnhGMAN2',
# ' __wpkreporterwid_=99a15c81-7d5d-4564-10ac-f47c09bdb24e; ubt_ssid=t58gahemosfi71dita0m0uetouticgzx_2020-06-07; perf_ssid=vv34jkbxp0h8yv2imr72fjy8h3t98eiy_2020-06-07; ut_ubt_ssid=cvdh6pyqtel17lboiy8hupzzm4v6k65o_2020-06-07; _bl_uid=0CkyObk95pn0jveehmC5kbd2ytCn; cna=hEZSF/sBiWwCAW8SLonGT2Q3; _utrace=08c6bfc14651d81f3160fd18ffa55b18_2020-06-07; l=eBQ4WpvrQVTtWzBKBO5ahurza77TCIRXGsPzaNbMiInca1rPaH520NQDdr1XudtjgtfjnhKyOvlFRRhBJPUU-AkDBeYBhSpT1xJwO; track_id=1591585829|0a059d2680501158c46a4fa943704d6113f4fe8d8c25ad0711|61bd29e095506cf9789f0d282ba40886; USERID=35820790; UTUSER=35820790; SID=CAAAAAACIpT26gAEAAD-ggzpA5Yck4-p1bh0xa87oFiSs0B2CegitIVP; ZDS=1.0|1591585829|CIT+yrzrGXkLRyQ5+hJ9NUDpTOm7XVWivyldfUinubl3ROmgmZApzXaR1DlqIbDd; isg=BIeH752WlcMJtBFOnDBXHsHwFjtRjFtuswU9g1l085Y9yK2KcFwBv5aJbo6WIDPm',
# # '__wpkreporterwid_=0d82cbd8-db95-4995-9329-08d0bba97ee0; ubt_ssid=clbpkimlzdtvo63wt1v1g8vhj58bezlt_2020-06-07; perf_ssid=78ftwxrjrelwt929cemjz932rs4ezcwp_2020-06-07; ut_ubt_ssid=7i7vwde0fbewfje8mh3nfw5qh8rehpcx_2020-06-07; cna=Mk7aFpUvjW8CAatfUbbpNZoR; _bl_uid=tIkzgbCL4w1yF3ah5kqRup932bU9; _utrace=3de7195594ca9a72bdd7d84e4ca62155_2020-06-07; track_id=1591527545|d3f1253063c2b881fbac5a3cc80654b25b36a151e0765f4e1f|901bcfb517f9d260ad4cf03f3dfe9cec; USERID=1000081239815; UTUSER=1000081239815; tzyy=8ef2905cc2c9185dc32c15e5ca11fe6b; t=1648e26109f1b0080f10cfdf036a35bd; l=eBOAeWbnQVNjALM_BO5Z-urza77O5IOXGsPzaNbMiInca6iAg3zigNQDpVW2zdtjgtfXrHtPOzL1BRHMSmUaSAkDBeYBhSpT1xJwr; SID=AgAAAOjZfK8H6gAEAABM6FaK0D553EKaBtZxdkXj1sBGWCuVH9Xrs7t9; ZDS=1.0|1591535160|4tVxKA+lM7OVQXrnFb7868Wt/ZdvA0x5DYPNMHoJ2204C97yz3FYcFXsvyfZdpYMNbufi8y/eZReX6/KylEfUw==; isg=BI6OUJnGXCVyD-gBMYpO3YBp32RQD1IJZH2wCbjX-hFNGy51IJ-iGTTZV0F3A0oh',
# '__wpkreporterwid_=249c2064-09b5-4290-bcec-0a17eabf779b; ubt_ssid=6d6qpdcn7b9sjznipypw8czstvve3nk0_2020-06-07; perf_ssid=mybj1vipvxutffy1qp26eoe0oarf0q4q_2020-06-07; ut_ubt_ssid=1volc20hbtfc2p9p85hshfpgmhml1ll6_2020-06-07; _bl_uid=30kjLb4k41Ota5iLhqLIn6Xha1Im; cna=6Y+HFU1bkwkCAXFcSe+3/nRa; _utrace=37ae7d1d02b017e173894fea3bb2efca_2020-06-07; track_id=1591519423|9a66bb685816851de95898ed6f3d3fcb52b5e1184c66fcd708|25703e329f8a6b21c9d4dc124f758010; USERID=121791358; UTUSER=121791358; tzyy=7b426df19e9be6ccce2b4eef498153d6; ZDS=1.0|1591532442|HNiWBJCKlJz5YhPNoaJXse+JBVZM1fVcayG+pi/cfgd9wmvw9ZvUZcmeFREdRnWl; l=eBNLpvaRQVjrxPMiBOfZlurza77TAIRfguPzaNbMiOCPO0Cp5YXFWZvQZkY9CnGVn6l6R35QyF69BSTorPa9Qxv9-e9bMdF_9dTh.; _samesite_flag_=true; cookie2=111dc5ffde4a524aab9b0720103582e8; t=aae572110ad9ca4cc9c0f57688d0ada0; _tb_token_=3d46efe35b97b; csg=2a0d59a5; t_eleuc4=id4=0%40BA%2FvuHCrrRkeMfkp7WOagoZAAZSmysPR%2F67zEA%3D%3D; munb=2204450098041; SID=AQAAAAAHQmN-7gAGPADLlfyNwQMeOR2O7ig_TL0YfBqYrRMpXzXis9Uc; x5check_ele=Xo0wsbZZGabt9fuUyE08370eWyIMWrI4CDGkffTiapc%3D; isg=BIOD8oD_2TfarZXCDfclhiUfEkct-Bc6USLtirVg3-JZdKOWPcinimHi6gI6VG8y_wpkreporterwid_=249c2064-09b5-4290-bcec-0a17eabf779b; ubt_ssid=6d6qpdcn7b9sjznipypw8czstvve3nk0_2020-06-07; perf_ssid=mybj1vipvxutffy1qp26eoe0oarf0q4q_2020-06-07; ut_ubt_ssid=1volc20hbtfc2p9p85hshfpgmhml1ll6_2020-06-07; _bl_uid=30kjLb4k41Ota5iLhqLIn6Xha1Im; cna=6Y+HFU1bkwkCAXFcSe+3/nRa; _utrace=37ae7d1d02b017e173894fea3bb2efca_2020-06-07; track_id=1591519423|9a66bb685816851de95898ed6f3d3fcb52b5e1184c66fcd708|25703e329f8a6b21c9d4dc124f758010; USERID=121791358; UTUSER=121791358;',
# #'__wpkreporterwid_=0d82cbd8-db95-4995-9329-08d0bba97ee0; ubt_ssid=clbpkimlzdtvo63wt1v1g8vhj58bezlt_2020-06-07; perf_ssid=78ftwxrjrelwt929cemjz932rs4ezcwp_2020-06-07; ut_ubt_ssid=7i7vwde0fbewfje8mh3nfw5qh8rehpcx_2020-06-07; cna=Mk7aFpUvjW8CAatfUbbpNZoR; _bl_uid=tIkzgbCL4w1yF3ah5kqRup932bU9; _utrace=3de7195594ca9a72bdd7d84e4ca62155_2020-06-07; track_id=1591527545|d3f1253063c2b881fbac5a3cc80654b25b36a151e0765f4e1f|901bcfb517f9d260ad4cf03f3dfe9cec; USERID=1000081239815; UTUSER=1000081239815; tzyy=8ef2905cc2c9185dc32c15e5ca11fe6b; t=1648e26109f1b0080f10cfdf036a35bd; l=eBOAeWbnQVNjALM_BO5Z-urza77O5IOXGsPzaNbMiInca6iAg3zigNQDpVW2zdtjgtfXrHtPOzL1BRHMSmUaSAkDBeYBhSpT1xJwr; SID=AgAAAOjZfK8H6gAEAABM6FaK0D553EKaBtZxdkXj1sBGWCuVH9Xrs7t9; ZDS=1.0|1591535160|4tVxKA+lM7OVQXrnFb7868Wt/ZdvA0x5DYPNMHoJ2204C97yz3FYcFXsvyfZdpYMNbufi8y/eZReX6/KylEfUw==; isg=BI6OUJnGXCVyD-gBMYpO3YBp32RQD1IJZH2wCbjX-hFNGy51IJ-iGTTZV0F3A0oh',
# '__wpkreporterwid_=88af1c50-d8a8-4cb1-b9a1-fc571e73c558; ubt_ssid=343qvjtvd5bd6n467fdr3cmvq4gyhmo7_2020-06-08; perf_ssid=e1003poworu7iduv9fc132tf4jpbvmpb_2020-06-08; ut_ubt_ssid=4vyv4ytylnfur6eixqb6j1pp7qt9i82z_2020-06-08; UTUSER=0; isg=BKKiGxidCCAkExT8sKTahVK18CgE86YNdOFLVew7zpXAv0I51IP2HSg9631DtB6l; l=eBMersSVQVUFgdydBOfChurza779xIObYuPzaNbMiOCP_gCM4MWNWZvQlGTHCn1Vnsh6R3yblDgJBvLa2Pa9Qxv9-e1Sm1uqbdTh.; _bl_uid=g0kkmbhO5ydvwph7mwFCrntreCk3; _utrace=d3ffa58aab14b811c27d9207f07dc736_2020-06-08; cna=W49kFzheOFoCAXW1ixk0Dik0; _samesite_flag_=true; cookie2=1197f681e708427978e2389b0a3f3611; t=06ddc36724da9da9328111fc53c6fe24; _tb_token_=f531ee3588a53',
'__wpkreporterwid_=0d82cbd8-db95-4995-9329-08d0bba97ee0; ubt_ssid=clbpkimlzdtvo63wt1v1g8vhj58bezlt_2020-06-07; perf_ssid=78ftwxrjrelwt929cemjz932rs4ezcwp_2020-06-07; ut_ubt_ssid=7i7vwde0fbewfje8mh3nfw5qh8rehpcx_2020-06-07; cna=Mk7aFpUvjW8CAatfUbbpNZoR; _bl_uid=tIkzgbCL4w1yF3ah5kqRup932bU9; _utrace=3de7195594ca9a72bdd7d84e4ca62155_2020-06-07; track_id=1591527545|d3f1253063c2b881fbac5a3cc80654b25b36a151e0765f4e1f|901bcfb517f9d260ad4cf03f3dfe9cec; USERID=1000081239815; UTUSER=1000081239815; tzyy=8ef2905cc2c9185dc32c15e5ca11fe6b; t=1648e26109f1b0080f10cfdf036a35bd; l=eBOAeWbnQVNjAnEiBO5ahurza77OoIOXfsPzaNbMiIncC6h5sl9T-s-QLs0fjpxRR8XcGa1y46aJ5OeTpFku7PDZndLHRKNvB5M2QK1..; SID=BQAAAOjZfK8H6gAEAADksZMUmFdTxXebSKZ0DPGPhsFsOEFUHINpr35H; ZDS=1.0|1591590064|4tVxKA+lM7OVQXrnFb7860blEdyVkhTqL2/ILrIBpCoZ+NGwcb+MQPEng2Pdl4n0uZy8vR6Not5CvRpOq+laPQ==; x5check_ele=3%2BtWw4b0faWQmcwhUT8MdKE2lK4VEFcF9XjanD%2F2OjQ%3D; isg=BOfnwyB_dSO5lfGucEmX-nE6dhuxbLtOFe6JJrlUA3asqAdqwTxLniXpzq42QJPG',
# '__wpkreporterwid_ "85cdaa51-03f6-4449-3176-007ebf5233c8"_bl_uid "enkjsbgq5g310L9LCzzvq6w89308"_utrace "fcba1c4cc41e0195a0e5d89a76422d9c_2020-06-07"cna "SfZXF8siVlECAXGKT/iUK9L"isg"BMTEtOivRmu4xPInVRmEG5YilkK23ehHhiF2qN5lFA9SCWXTBu_A1wDnSSHRCiCf"l"eBSsZzNuQVTu3IcFKOfChurza779IObYuPzaNbMiOCP3595mX5WZvK8NLpCn1VnsF2R3yblDgJBbYspyUB5Lis8wJbMdF_hdTh."munb"2205036748408"perf_ssid "gukahawss1ifn1g0jz975jspmdb4hpcy_2020-06-07"SID "DAAAAABOlXFC7AAGbAA0r4UFKiwcU8iPpMkmEdaLO41vAdxb5lLG8qy4"t "b954103b2de58bd2949999eb3175e150"t_eleuc4 "id4=0@BAvuHCrrRj3bMwlc00qlU3R6lCX1cYbBFPuvw=="tzyy "1c48c11327fa016b2049a00464044e7d"ubt_ssid "oeqt8ber6eopq43fqjz2tv50fimbyyva_2020-06-07"USERID"1318416706"ut_ubt_ssid "35sedh8xdv585tnviocccqgpekjr4xxv_2020-06-07"UTUSER "1318416706"x5check_ele "Ym75BDvxtuUyVonRhpbJrA0kzdKrA8OLjcx2hx+RWnE="',
]
host = [
#     '219.137.143.121',
#     '113.116.94.241',
#     '14.152.19.82',
#     '113.64.153.227',
#     # '4',
#     # '5',
#     '120.229.56.77',
#     # '7',
#     '27.187.78.30',
#     '120.230.181.156',
#     '113.83.33.116',
#     '111.19.36.155',
#     # '12',
#     '113.92.73.169',
#     # '14',
#     '47.92.62.13',
    '110.185.157.76',
#     '113.138.76.147',
]
while True:
    try:
        group_ID = offset%len(cookie)#组员ID
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': cookie[group_ID],
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Mobile Safari/537.36',
            'x-shard': 'loc=116.322056,39.89491'
        }
        url = 'https://h5.ele.me/restapi/shopping/v3/restaurants?latitude=39.89491&longitude=116.322056&offset={}&limit=18'.format(offset)
#         proxies = get_ip()
        proxyMeta = "http://%(host)s:%(port)s" % {
            "host" : hsot[group_ID],
            "port" : '8888',
        }
        proxies = {
            "http" : proxyMeta,
        }
        time.sleep(random.randint(2,4))
        text = requests.get(url,headers=headers,proxies=proxies).text#
#         release_ip()
        text_json = json.loads(text)
        for i in range(len(text_json['items'])):
            str_s = json.dumps(text_json['items'][i]['restaurant'],ensure_ascii=False)+'\n'
            with open('Shop.json','a',encoding='utf-8')as f:
                f.write(str_s)
            shop_id.append(text_json['items'][i]['restaurant']['id'])
        print('第{}页商铺ID获取成功...'.format(offset))
        offset+=1
    except Exception as e:
        if shop_id==[]:
            print('第{}页商铺ID信息获取失败,请更换组员ID[{}]的cookie！'.format(offset,group_ID))
            result = str(input('请输入新的cookie:'))
            if result!= str(-1):
                cookie[group_ID] = result
            else:
                break
#                 offset+=1
            continue
        elif '请登录'in text:
            print('第{}页商铺ID信息获取失败,请更换组员ID[{}]的cookie！'.format(offset,group_ID))
            result = str(input('请输入新的cookie:'))
            if result!= str(-1):
                cookie[group_ID] = result
            else:
                break
#                 offset+=1
            continue
#             print('获取失败')
#             break
        elif '"rgv587_flag": "sm"'in text:
            print('第{}页商铺ID信息获取失败,请更换组员ID[{}]的cookie！'.format(offset,group_ID))
            result = str(input('请输入新的cookie:'))
            if result!= str(-1):
                cookie[group_ID] = result
            else:
                break
#                 offset+=1
            continue
        else:
            print(text)
            print('该经纬度店铺id获取完成！')
            break
print(shop_id)