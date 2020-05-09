
from bs4 import BeautifulSoup

html = """<ul class="item_con_list">
                                                        <li class="con_list_item default_list" data-index="0" data-positionid="5502041" data-salary="25k-40k" data-company="招银网络科技" data-positionname="Java开发工程师" data-companyid="32720" data-hrid="1594940" data-adword="9">
                                             <span class="top_icon hurry_up"></span>
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/5502041.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="0" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="5502041" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>深圳·南山区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">1天前发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">25k-40k</span>
                                    <!--<i></i>-->经验1-3年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/32720.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="32720" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">招银网络科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                金融 / 不需要融资 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/32720.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0101
                                                                                        " data-lg-tj-cid="32720" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/A5/6B/Cgp3O1ir8wOAJzPbAAIHeppEuoE288.png" alt="招银网络科技" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>银行</span>
                                                                    <span>后端</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“大平台 行业领先 福利待遇好”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="1" data-positionid="7113784" data-salary="30k-50k" data-company="新分享科技服务" data-positionname="java开发组长" data-companyid="212814" data-hrid="12729182" data-adword="9">
                                             <span class="top_icon hurry_up"></span>
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/7113784.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="7113784" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">java开发组长</h3>
                                                                                                                                                                        <span class="add">[<em>深圳·南油</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:03发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">30k-50k</span>
                                    <!--<i></i>-->经验5-10年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/212814.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="212814" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">新分享科技服务</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                金融 / B轮 / 50-150人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/212814.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0102
                                                                                        " data-lg-tj-cid="212814" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/9B/83/CgoB5lvGnnKARKVSAAAaSAZL_Uw255.png" alt="新分享科技服务" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>互联网金融</span>
                                                                    <span>后端</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“高成长高发展空间，欢迎加入，一起成长。”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="2" data-positionid="4770607" data-salary="15k-25k" data-company="腾讯" data-positionname="Java高级开发工程师" data-companyid="451" data-hrid="7349721" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/4770607.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="4770607" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java高级开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>北京·北京大…</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:08发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/451.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="451" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">腾讯</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                社交 / 上市公司 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/451.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0103
                                                                                        " data-lg-tj-cid="451" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/00/03/CgYXBlTUV_qALGv0AABEuOJDipU378.jpg" alt="腾讯" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>分布式</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“鹅厂好福利,大平台,大咖多”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="3" data-positionid="7020203" data-salary="18k-30k" data-company="微创软件" data-positionname="java开发工程师" data-companyid="124652" data-hrid="12069320" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/7020203.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="3" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="7020203" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>上海·五角场</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">09:47发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">18k-30k</span>
                                    <!--<i></i>-->经验5-10年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/124652.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="124652" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">微创软件</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,移动互联网 / 不需要融资 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/124652.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0104
                                                                                        " data-lg-tj-cid="124652" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/28/D8/CgotOVzPyauAMybNAAA8zQprrtk576.jpg" alt="微创软件" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>云计算</span>
                                                                    <span>大数据</span>
                                                                    <span>后端</span>
                                                                    <span>分布式</span>
                                                                    <span>docker</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“六险一金工作环境nice技术前沿”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="4" data-positionid="6994039" data-salary="9k-17k" data-company="微创软件" data-positionname="java开发工程师" data-companyid="124652" data-hrid="12069320" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6994039.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="4" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="6994039" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>杭州·西兴</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">09:47发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">9k-17k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/124652.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="124652" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">微创软件</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,移动互联网 / 不需要融资 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/124652.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0105
                                                                                        " data-lg-tj-cid="124652" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/28/D8/CgotOVzPyauAMybNAAA8zQprrtk576.jpg" alt="微创软件" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>汽车</span>
                                                                    <span>大数据</span>
                                                                    <span>后端</span>
                                                                    <span>J2EE</span>
                                                                    <span>Java</span>
                                                                    <span>算法</span>
                                                                                    </div>
                        <div class="li_b_r">“六险一金工作环境nice技术前沿”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="5" data-positionid="5699653" data-salary="25k-50k" data-company="字节跳动" data-positionname="Java开发工程师" data-companyid="62" data-hrid="8751754" data-adword="0">
                                         <span class="top_icon direct_recruitment" style="display: inline;"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/5699653.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="5" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="5699653" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>北京·海淀区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">09:39发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">25k-50k</span>
                                    <!--<i></i>-->经验1-3年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/62.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="62" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">字节跳动</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                文娱丨内容 / C轮 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/62.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0106
                                                                                        " data-lg-tj-cid="62" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/79/0A/CgoB5ltr2A-AM5SFAADbT9jQCn841.jpeg" alt="字节跳动" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>后端开发</span>
                                                                                    </div>
                        <div class="li_b_r">“六险一金，弹性工作，免费三餐，租房补贴”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="6" data-positionid="6647196" data-salary="30k-50k" data-company="字节跳动" data-positionname="Java开发工程师" data-companyid="62" data-hrid="8751754" data-adword="0">
                                         <span class="top_icon direct_recruitment" style="display: inline;"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6647196.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="6" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="6647196" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>杭州·余杭区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">09:38发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">30k-50k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/62.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="62" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">字节跳动</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                文娱丨内容 / C轮 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/62.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0107
                                                                                        " data-lg-tj-cid="62" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/79/0A/CgoB5ltr2A-AM5SFAADbT9jQCn841.jpeg" alt="字节跳动" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                                                        <span>扁平管理</span>
                                                                                                                                                <span>弹性工作</span>
                                                                                                                                                <span>大厨定制三餐</span>
                                                                                                                                                <span>就近租房补贴</span>
                                                                                                                        </div>
                        <div class="li_b_r">“六险一金”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="7" data-positionid="5401616" data-salary="15k-30k" data-company="腾讯" data-positionname="java开发工程师" data-companyid="451" data-hrid="14158063" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/5401616.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="7" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="5401616" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>深圳·南山区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">09:27发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-30k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/451.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="451" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">腾讯</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                社交 / 上市公司 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/451.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0108
                                                                                        " data-lg-tj-cid="451" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/00/03/CgYXBlTUV_qALGv0AABEuOJDipU378.jpg" alt="腾讯" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“技术大咖”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="8" data-positionid="6972144" data-salary="25k-50k" data-company="阅文集团" data-positionname="JAVA开发工程师" data-companyid="28243" data-hrid="370271" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6972144.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="8" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="6972144" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">JAVA开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>上海·张江</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">09:08发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">25k-50k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/28243.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="28243" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">阅文集团</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                文娱丨内容 / 上市公司 / 500-2000人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/28243.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0109
                                                                                        " data-lg-tj-cid="28243" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/66/AB/CgpFT1mnc9qAW5utAAAZPTBrPD4069.png" alt="阅文集团" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“上市公司”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="9" data-positionid="7031477" data-salary="20k-30k" data-company="东辰网络" data-positionname="高级java开发工程师" data-companyid="753587" data-hrid="8632300" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/7031477.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="9" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="7031477" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">高级java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>广州·车陂</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:16发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">20k-30k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/753587.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="753587" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">东辰网络</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                软件开发 社交 / 不需要融资 / 50-150人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/753587.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0110
                                                                                        " data-lg-tj-cid="753587" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M01/6D/8C/CgotOV1BgPWAa0naAAAkBnHYz-A932.png" alt="东辰网络" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>社交</span>
                                                                    <span>后端</span>
                                                                    <span>服务器端</span>
                                                                    <span>客户端</span>
                                                                                    </div>
                        <div class="li_b_r">“五险一金 带薪年假 年度体检 年终奖”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="10" data-positionid="6749711" data-salary="20k-40k" data-company="阅文集团" data-positionname="Java高级开发工程师" data-companyid="28243" data-hrid="370271" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6749711.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="10" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="6749711" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java高级开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>北京·亚运村</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">09:07发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">20k-40k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/28243.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="28243" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">阅文集团</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                文娱丨内容 / 上市公司 / 500-2000人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/28243.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0111
                                                                                        " data-lg-tj-cid="28243" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/66/AB/CgpFT1mnc9qAW5utAAAZPTBrPD4069.png" alt="阅文集团" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>后端</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“大平台、领导nice、福利好”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="11" data-positionid="7119056" data-salary="10k-15k" data-company="联龙博通" data-positionname="java开发工程师" data-companyid="17785" data-hrid="15049483" data-adword="0">
                                         <span class="top_icon direct_recruitment" style="display: inline;"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/7119056.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="11" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="7119056" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">java开发工程师</h3>
                                                                                                                                                                        <span class="add">[<em>杭州·江南</em>]</span>
                                                                                                                                                        </a>
                                <span class="format-time">10:13发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">10k-15k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/17785.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="17785" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">联龙博通</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,电商 / D轮及以上 / 2000人以上
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/17785.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0112
                                                                                        " data-lg-tj-cid="17785" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/1E/06/CgYXBlUs4zKABvsqAACmSrJc6MQ571.jpg" alt="联龙博通" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“年终奖 上升空间大”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="12" data-positionid="6835224" data-salary="12k-20k" data-company="科来" data-positionname="Java开发工程师" data-companyid="63063" data-hrid="8755412" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6835224.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="12" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="6835224" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">Java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>成都·高新区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">10:11发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">12k-20k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/63063.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="63063" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">科来</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,其他 / A轮 / 150-500人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/63063.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0113
                                                                                        " data-lg-tj-cid="63063" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/image1/M00/1E/02/Cgo8PFUs2NSAN1ToAAAzgI4Awu8947.jpg" alt="科来" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>分布式</span>
                                                                    <span>J2EE</span>
                                                                    <span>中间件</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“15薪 职业发展 领导nice”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="13" data-positionid="6789259" data-salary="15k-25k" data-company="惠合" data-positionname="高级java开发工程师" data-companyid="180930" data-hrid="4111374" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6789259.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="13" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="6789259" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">高级java开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>杭州·西湖区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">09:54发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">15k-25k</span>
                                    <!--<i></i>-->经验3-5年 / 本科
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/180930.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="180930" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">惠合</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                移动互联网,企业服务 / A轮 / 50-150人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/180930.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0114
                                                                                        " data-lg-tj-cid="180930" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image/M00/51/49/CgpEMlly8N-AKz8gAAA8zdGJFsg496.png" alt="惠合" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>电商</span>
                                                                    <span>新零售</span>
                                                                    <span>后端</span>
                                                                    <span>服务器端</span>
                                                                    <span>Linux/Unix</span>
                                                                    <span>客户端</span>
                                                                                    </div>
                        <div class="li_b_r">“环境好，氛围好，老板好，福利好”</div>
                    </div>
                </li>
                                                            <li class="con_list_item default_list" data-index="14" data-positionid="6899439" data-salary="10k-18k" data-company="深圳市智能制造软件开发有限公司" data-positionname="JAVA开发工程师" data-companyid="198438" data-hrid="15847433" data-adword="0">
                                         <span class="top_icon direct_recruitment"></span>
                    <div class="list_item_top">
                        <div class="position">
                            <div class="p_top">

                                <a class="position_link" href="https://www.lagou.com/jobs/6899439.html?show=4b9f388b65c94be78eb258d38ae74b0a" target="_blank" data-index="14" data-lg-tj-id="8E00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="6899439" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0" data-lg-webtj-_show_id="4b9f388b65c94be78eb258d38ae74b0a" data-lg-webtj-_search_type="csearch" data-lg-webtj-_content_type="jd">
                                    <h3 style="max-width: 180px;">JAVA开发工程师</h3>
                                                                                                                                                                                                                            <span class="add">[<em>深圳·南山区</em>]</span>
                                                                                                                                                                                                        </a>
                                <span class="format-time">09:27发布</span>
                            </div>
                            <div class="p_bot">
                                <div class="li_b_l">
                                    <span class="money">10k-18k</span>
                                    <!--<i></i>-->经验3-5年 / 大专
                                </div>
                            </div>
                        </div>
                        <div class="company">
                            <div class="company_name">
                                <a href="https://www.lagou.com/gongsi/198438.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="198438" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">深圳市智能制造软件开发有限公司</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                            </div>
                            <div class="industry">
                                企业服务,消费生活 / B轮 / 50-150人
                            </div>
                        </div>
                        <div class="com_logo">
                            <a href="https://www.lagou.com/gongsi/198438.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="
                                                                                                0115
                                                                                        " data-lg-tj-cid="198438" data-lg-tj-abt="dm-csearch-showCountPositionStrategy|0">
                                                                <img src="//www.lgstatic.com/thumbnail_120x120/i/image2/M00/44/13/CgoB5lrLAb-AIlYXAAAtt9Uattc709.png" alt="深圳市智能制造软件开发有限公司" width="60" height="60">
                                                            </a>
                        </div>
                    </div>
                    <div class="list_item_bot">
                        <div class="li_b_l">
                                                                                                <span>MySQL</span>
                                                                    <span>Java</span>
                                                                                    </div>
                        <div class="li_b_r">“公司福利多多”</div>
                    </div>
                </li>
                                                                                                </ul>
"""
soup = BeautifulSoup(html,"lxml")

# 1.获取所有tr标签
# trs = soup.find_all('li')
# for tr in trs:
#     print(tr)

# #2.获取第二个tr标签
# tr = soup.find_all('li',limit=2)[1]
# print(tr)

#3.获取所有class等于even的tr标签
# trs = soup.find_all('li',attrs={'class':"even"})
# for tr in trs:
#     print(tr)

#4.将所有id等于test，class也等于test的a标签提取出来
aList = soup.find_all('a',id='test',class_='test')
aList = soup.find_all('a',attrs={"id":"test","class":"test"})
for a in aList:
    print(a)

#获取所有的职位信息
trs = soup.find_all('tr')[1:]
movies=[]
for tr in trs:
    movie = {}
    tds = tr.find_all("td")
    title = tds[0].string
    city = tds[3].string
    movie['title'] = title
    movie['city'] = city
    movies.append(movie)

    infos = list(tr.stripped_strings)
    movie['title'] = infos[0]
    movie['city'] = infos[3]


## 使用find 和find_all的过滤条件
#   1.关键字参数:将属性的名字作为关键字参数的名字，以及属性的值作为关键字参数的值进行过滤
#   2.attrs参数:将属性条件放到一个字典中，传给attrs参数

#   strings和stripped_strings,string属性以及get_text方法
# 1.String：获取某个标签下的非标签字符串，返回来的是字符串
# 2.strings:获取某个标签下的子孙非标签字符串，返回来的是生成器
# 3.stripped_strings:获取某个标签下的子孙非标签字符串，会去掉空白字符，返回来的是个生成器
# 4：get_text:获取某个标签下的子孙非标签字符串，不是以列表的形式返回，是以普通字符串返回
