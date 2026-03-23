"""
    将常用元素进行封装

"""
from selenium.webdriver.common.by import By

'''
一、登录页面
'''
#用户名输入框
page_login_user = ["xpath",'/html/body/div[1]/div/div/div[2]/div/form/div[1]/div/div[1]/div/input']

#密码输入框
page_login_indexPwd = ["xpath","/html/body/div[1]/div/div/div[2]/div/form/div[2]/div/div[1]/div/input"]

#登录按钮
page_login_loginBtn = ["xpath",'/html/body/div[1]/div/div/div[2]/div/form/div[3]/div/button/span']

'''
二.菜单
'''
#机动部静设备工作台
#生产运行部设备工程师工作台
    #待办页面处理按钮
sby_gzt_db_cl=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/button/span"]
    #待办页面处理弹窗确认按钮
sby_gzt_db_cl_qr=["xpath","/html/body/div[10]/div/div/div[3]/button/span"]
    #定力矩服务计划页面 下派 按钮
sby_gzt_db_cl_fb=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div[1]/div/div[2]/button[1]/span"]
    #检修范围添加确认页面
        #同意按钮
sby_gzt_db_jxfwqr_ty=["xpath",""]
        #驳回按钮
sby_gzt_db_jxfwqr_bh=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[3]/div[1]/div/div/div[2]/button/span/span"]
        #驳回确认弹窗-确认按钮
sby_gzt_db_jxfwqr_bh_qr=["xpath","/html/body/div[4]/div/div/div[3]/button[2]/span"]
#服务商负责人工作台
    #待办页面
        #处理按钮
fws_fzr_gzt_db_cl=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div[2]/button/span"]
    #项目立项确认页面
        #下一步按钮
fws_fzr_lxqr_xyb=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[3]/div/div[3]/button/span"]
        #项目经理选择框
fws_fzr_lxqr_xmjl=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[3]/div/form/div[1]/div/div/div/div[1]/div[1]/input"]
        #缺认按钮
fws_fzr_lxqr_qr=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[3]/div/div/button[2]/span"]
#项目经理工作台
    #待办页面
    #处理按钮
xmjl_gzt_db_cl=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/button/span"]
    #提示界面-确认按钮
xmjl_gzt_db_ts_qr=["xpath","/html/body/div[12]/div/div/div[3]/button/span"]
#项目管理页面
    #成员配置按钮
xmgl_cypz=["xpath","//span[text()='成员配置']/parent::button"]
        #成员配置页面
            #添加按钮
xmgl_cypz_tj=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/button[1]/span"]
            #添加页面展开箭头
xmgl_cypz_tj_xl=["xpath","/html/body/div[6]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[1]/i"]
            #选择人员
xmgl_cypz_tj_03=["xpath","/html/body/div[6]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div[2]/div[3]/div/label/span/span"]
            #确定按钮
xmgl_cypz_tj_qd=["xpath","/html/body/div[6]/div/div/footer/div/button[2]/span"]
            #返回按钮
xmgl_cypz_fh=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/button/span"]
    #推送设备员按钮
xmgl_tssby=["xpath","//span[text()='推送设备员确认']/parent::button"]
    #检修范围按钮
xmgl_jxfw=["xpath","//span[text()='检修范围']/parent::button"]
        #下一页按钮
xmgl_jxfw_xyy=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[4]/button[2]/i"]
        #全选
xmgl_jxfw_gx_qx=["xpath",'<span class="el-checkbox__input"><input class="el-checkbox__original" type="checkbox" id="el-id-429-2327"><span class="el-checkbox__inner"></span></span>']
        #勾选1
xmgl_jxfw_gx_01=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/label/span/span"]
        #提交按钮
xmgl_jxfw_tj=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/button[1]/span"]
        #提交页面-确认按钮
xmgl_jxfw_tj_qr=["xpath","/html/body/div[7]/div/div/div[3]/button[2]/span"]
        #返回按钮
xmgl_jxfw_fh=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[1]/div[2]/button/span"]
    # 角色配置
xmgl_jspz=["xpath","//span[text()='角色配置']/parent::button"]
    # 压测
xmgl_yc=["xpath","//span[text()='压测']/parent::button"]
    #结项
xmgl_jx=["xpath","//span[text()='结项']/parent::button"]
xmgl_jx_=["xpath","//span[text()='上传结项材料']/parent::button"]
xmgl_jx_=["xpath",""]
xmgl_jx_=["xpath",""]

    # 返回
xmgl_fh=["xpath","//span[text()='返回']/parent::button"]
#服务计划管理
fwjh =["xpath","/html/body/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]/div/span"]
    #定力矩服务计划
fwjh_dljfwjh =["xpath","/html/body/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]/ul/li[2]/span"]
        #添加按钮
fwjh_dljfwjh_tj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/button/span"]
            #年月
fwjh_dljfwjh_ny =["xpath",]
            #计划名称
fwjh_dljfwjh_jhmc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[1]/form/div/div[2]/div/div/div/div/input"]
            #检修类型
fwjh_dljfwjh_jxlx =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[1]/form/div/div[3]/div/div/div/div/div[1]/div[2]/span"]
            #计划开始日期
fwjh_dljfwjh_kssj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[1]/form/div/div[4]/div/div/div/div/input"]
            #计划结束日期
fwjh_dljfwjh_jssj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[1]/form/div/div[5]/div/div/div/div/input"]
            #关联进行中计划
fwjh_dljfwjh_gljxzjh =["xpath",]
            #关联历史计划
fwjh_dljfwjh_gllsjh =["xpath",]
            #启用监理
fwjh_dljfwjh_qyjl =["xpath",]
            #监理方
fwjh_dljfwjh_jlf =["xpath",]
            #保存按钮
fwjh_dljfwjh_bc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[1]/div[2]/button/span"]
            #下派按钮
fwjh_dljfwjh_xp =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[1]/div/div[2]/button[1]/span"]
        # 检修范围配置
            #添加按钮
fwjh_dljfwjh_jxfwpz_tj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[8]/div[2]/div[1]/div/div/section[2]/div[2]/div/div/button[1]/span"]
            #服务商
fwjh_dljfwjh_jxfwpz_fws =["xpath","/html/body/div[4]/div/div/div/form/div/div[1]/div/div/div/div/div[1]/div[1]"]
                #装置
fwjh_dljfwjh_jxfwpz_zz =["xpath","/html/body/div[4]/div/div/div/form/div/div[2]/div/div/div/div/div[1]/div[1]"]
                #装置法兰总量
fwjh_dljfwjh_jxfwpz_zzflzl =["xpath",""]
                #计划检修量
fwjh_dljfwjh_jxfwpz_jhjxl =["xpath","/html/body/div[4]/div/div/div/form/div/div[4]/div/div/div/div/input"]
                #服务模式
fwjh_dljfwjh_jxfwpz_fwms =["xpath","/html/body/div[4]/div/div/div/form/div/div[5]/div/div/div/div/div[1]/div[2]"]
                #确定按钮
fwjh_dljfwjh_jxfwpz_qd =["xpath","/html/body/div[4]/div/div/footer/button[2]/span"]
                #取消按钮
fwjh_dljfwjh_jxfwpz_qx =["xpath","/html/body/div[4]/div/div/footer/button[1]/span"]
            #批量删除按钮
fwjh_dljfwjh_jxfwpz_plsc =["xpath",]
            #编辑
fwjh_dljfwjh_jxfwpz_bj =["xpath",]
            #删除
fwjh_dljfwjh_jxfwpz_sc =["xpath",]
            #法兰配置
                #返回
fwjh_dljfwjh_jxfwpz_flpz_fh =["xpath",]
                #已选
fwjh_dljfwjh_jxfwpz_flpz_yx =["xpath",]
                #未选
fwjh_dljfwjh_jxfwpz_flpz_wx=["xpath",]
                    #关键字
fwjh_dljfwjh_jxfwpz_flpz_gjz =["xpath",]
                    #查询
fwjh_dljfwjh_jxfwpz_flpz_cx =["xpath",]
                    #重置
fwjh_dljfwjh_jxfwpz_flpz_cz =["xpath",]
                    #提交
fwjh_dljfwjh_jxfwpz_flpz_tj =["xpath",]
                    #下载模板
fwjh_dljfwjh_jxfwpz_flpz_xzmb =["xpath",]
                    #上传
fwjh_dljfwjh_jxfwpz_flpz_sc =["xpath",]
                    #翻页
fwjh_dljfwjh_jxfwpz_flpz_fy =["xpath",]

"""
APP页面
"""
#登录
#账号
#用户名输入框
page_login_user_app = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[1]/uni-view[1]/uni-input/div/input"]

#密码输入框
page_login_indexPwd_app = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[1]/uni-view[2]/uni-view/uni-input/div/input"]
#登录按钮
page_login_loginBtn_app = ["xpath","/html/body/div/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[1]/uni-view[3]"]
#密码
'''
    定力矩服务
'''
#工序处理模块
app_dljfw_gxcl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view/uni-view[2]/uni-view[2]/uni-view[1]"]
    #待领取页签
app_dljfw_gxcl_dlq =["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/div[2]/div[1]/text()"]
        #勾选框第一个
app_dljfw_gxcl_dlq_01=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[2]/uni-scroll-view/div/div/div/uni-view[1]/uni-view/uni-view/uni-view[1]/uni-image"]
        #领取按钮
app_dljfw_gxcl_dlq_lq=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-view[2]"]
    #待处理页签
app_dljfw_gxcl_dcl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/div[2]/div[2]"]
        #第一个工序
app_dljfw_gxcl_dcl_dj_01=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[2]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-view[1]"]

#工序任务页面
#项目名称
app_gxcl_xmmc =['xpath','/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/div[1]']
    #输入框查询
app_gxcl_xmmc_srk=['xpath',"//div[contains(@class, 'model-item') and contains(text(), '2026年03月新测试流程北京源诚')]"]
    #法兰挂牌
app_gxrw_flgp=["xpath",'//uni-view[contains(@class, "process-item") and text()="法兰挂牌"]']
        #法兰挂牌照片
app_gxrw_flgp_flgpzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[1]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #法兰层级
app_gxrw_flgp_cj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[2]/uni-view[2]/uni-input/div/input"]
        #提交
app_gxrw_flgp_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #保存
app_gxrw_flgp_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]

    #法兰拆卸
app_gxrw_flcx=["xpath",'//uni-view[contains(@class, "process-item") and text()="法兰拆卸"]']
        #工具类型
app_gxrw_flcx_gjlx=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[1]/uni-view[2]/uni-picker"]
        #工具型号
app_gxrw_flcx_gjxh=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[2]/uni-view[2]/uni-picker"]
        #拆卸方式
app_gxrw_flcx_cxfs=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[3]/uni-view[2]/uni-picker"]
        #拆卸工具数量
app_gxrw_flcx_cxgjsl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[4]/uni-view[2]/uni-view/uni-input/div/input"]
        #拆卸拉伸力
app_gxrw_flcx_cxlsl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view[2]/uni-view/uni-input/div/input"]
        #拆卸后照片
app_gxrw_flcx_cxhzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #技术人员
app_gxrw_flcx_jsry_jsry=["xpath",""]
        #施工人员
app_gxrw_flcx_sgry=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[17]/uni-view[2]/uni-view/uni-view/uni-view/uni-input/div/input"]
        #保存
app_gxrw_flcx_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
app_gxrw_flcx_=["xpath",""]



    #密封面检查
app_gxrw_mfmjc=["xpath",'//uni-view[contains(@class, "process-item") and text()="密封面检查"]']
        #保存
app_gxrw_mfmjc_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
app_gxrw_mfmjc_=["xpath",""]
app_gxrw_mfmjc_=["xpath",""]

        #密封面照片
app_gxrw_mfmjc_mfmzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[19]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #提交按钮
app_gxrw_mfmjc_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
    #垫片检查
app_gxrw_dpjc =["xpath",'//uni-view[contains(@class, "process-item") and text()="垫片检查"]']
app_gxrw_dpjc_ =["xpath",""]
app_gxrw_dpjc_ =["xpath",""]
app_gxrw_dpjc_ =["xpath",""]
app_gxrw_dpjc_ =["xpath",""]
app_gxrw_dpjc_ =["xpath",""]
app_gxrw_dpjc_ =["xpath",""]

        #垫片照片
app_gxrw_dpjc_dpzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[11]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #垫片规格铭牌
app_gxrw_dpjc_dpgemp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[12]/uni-view/uni-view/uni-view/uni-view/uni-view/uni-view[2]"]
        #提交按钮
app_gxrw_dpjc_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
    #紧固件检查
app_gxrw_jgjjc=["xpath",'//uni-view[contains(@class, "process-item") and text()="紧固件检查"]']
        #保存
app_gxrw_jgjjc_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
app_gxrw_jgjjc_=["xpath",""]
app_gxrw_jgjjc_=["xpath",""]
app_gxrw_jgjjc_=["xpath",""]
app_gxrw_jgjjc_=["xpath",""]

        #螺栓螺母照片
app_gxrw_jgjjc_lslmzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[12]/uni-view/uni-view/uni-view/uni-view/uni-view/uni-view[2]"]
        # 提交按钮
app_gxrw_jgjjc_dpjc_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
    #预装确认
app_gxrw_yzqr=["xpath",'//uni-view[contains(@class, "process-item") and text()="预装确认"]']
        # 提交按钮
app_gxrw_yzqr_dpjc_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #紧固照片
app_gxrw_yzqr_jgzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[10]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #保存
app_gxrw_yzqr_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
        #提交
app_gxrw_yzqr_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
app_gxrw_yzqr_=["xpath",""]
app_gxrw_yzqr_=["xpath",""]
app_gxrw_yzqr_=["xpath",""]

    #SOP确认
app_gxrw_sopqr=["xpath","//uni-view[contains(@class, 'process-item') and text()='SOP确认']"]
     #保存
app_gxrw_sopqr_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
app_gxrw_sopqr_ =["xpath",""]
app_gxrw_sopqr_ =["xpath",""]
app_gxrw_sopqr_ =["xpath",""]
app_gxrw_sopqr_ =["xpath",""]

        # 提交按钮
app_gxrw_sopqr_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #工具类型
app_gxrw_sopqr_gjlx=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[1]/uni-view[2]/uni-picker/div[2]/uni-view/uni-view"]
            #工具类型—液压方驱扳手
app_gxrw_sopqr_gjlx_yyfq=["xpath","/html/body/div[1]/uni-app/div/div[2]/div[2]/div[1]"]
            #工具类型-完成按钮
app_gxrw_sopqr_gjlx_wc=["xpath","/html/body/div[1]/uni-app/div/div[2]"]
        #工具型号
app_gxrw_sopqr_gjxh=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[2]/uni-view[2]"]
            #工具型号-LFTW-03
            # 完成按钮
app_gxrw_sopqr_gjxh_wc=["xpath","/html/body/div[1]/uni-app/div/div[2]/div[1]/div[2]"]
        #螺母对边
app_gxrw_sopqr_lmdb=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[3]/uni-view[2]"]
        #工具数量
app_gxrw_sopqr_gjsl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[4]/uni-view[2]/uni-view/uni-input/div/input"]
        #新旧螺栓确认
app_gxrw_sopqr_xjlsqr=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view[2]"]
            # 完成按钮
app_gxrw_sopqr_gjxh_wc = ["xpath", "/html/body/div[1]/uni-app/div/div[2]/div[1]/div[2]"]
        #润滑剂确认
app_gxrw_sopqr_rhjqr=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[6]/uni-view[2]"]
        #螺栓工况确认
app_gxrw_sopqr_lsgkqr=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view[2]"]
        #法兰面工况
app_gxrw_sopqr_flmgk=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[8]/uni-view[2]"]
        #摩擦系数
app_gxrw_sopqr_mcxs=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[9]/uni-view[2]/uni-view/uni-input/div/input"]
        #T1A
app_gxrw_sopqr_T1A=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[10]/uni-view[2]/uni-view/uni-input/div/input"]
        #T1B
app_gxrw_sopqr_T1B=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[11]/uni-view[2]/uni-view/uni-input/div/input"]
        #A压
app_gxrw_sopqr_Ay=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[12]/uni-view[2]/uni-view/uni-input/div/input"]
        #B压
app_gxrw_sopqr_By=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[13]/uni-view[2]/uni-view/uni-input/div/input"]
         #预紧力推荐值
app_gxrw_sopqr_yjltjz=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[14]/uni-view[2]"]
        #实际施工值
app_gxrw_sopqr_sjsgz=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[15]/uni-view[2]"]

    #法兰抽检
app_gxrw_flcj=["xpath","//uni-view[contains(@class, 'process-item') and text()='法兰抽检']"]
        # 提交按钮
app_gxrw_flcj_dpjc_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #紧固压力
app_gxrw_flcj_jgyl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[3]/uni-view[2]/uni-view/uni-input/div/input"]
        #抽检前照片
app_gxrw_flcj_cjqzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[4]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #抽检公差
app_gxrw_flcj_cjgc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view/uni-view[2]/uni-view/uni-view[1]/uni-view"]
            #确定
app_gxrw_flcj_cjgc_qd=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-button[2]"]
        #校验公差1
app_gxrw_flcj_jygc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view/uni-view[2]/uni-view/uni-view[1]"]
            #确定
app_gxrw_flcj_jygc_qd=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-button[2]"]
        #校验公差2
app_gxrw_flcj_jygc_2=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[10]/uni-view/uni-view[2]/uni-view/uni-view[1]"]
            #确定
app_gxrw_flcj_jygc_qd_2=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[10]/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-button[2]"]
        #抽检过程照片
app_gxrw_flcj_cjgczp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[12]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #保存
app_gxrw_flcj_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
        #提交
app_gxrw_flcj_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
app_gxrw_flcj_=["xpath",""]

    #完工确认
app_gxrw_wgqr=["xpath","//uni-view[contains(@class, 'process-item') and text()='完工确认']"]
        #垫片照片
app_gxrw_wgqr_dpzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #提交
app_gxrw_wgqr_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #保存
app_gxrw_wgqr_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
app_gxrw_wgqr_=["xpath",""]

        # 提交按钮
app_gxrw_wgqr_dpjc_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #平行公差
app_gxrw_wgqr_pxgc=["xpath",""]
        #公差值
app_gxrw_wgqr_gcz=["xpath",""]
        #垫片受压状态是否异常
app_gxrw_wgqr_dpsyzt=["xpath",""]
        #垫片照片
app_gxrw_wgqr_dpzp=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view/uni-view/uni-view/uni-view/uni-view"]
        #保存
app_gxrw_wgqr_bc=["xpath",""]
    #法兰校核
app_gxrw_fljh=["xpath","//uni-view[contains(@class, 'process-item') and text()='法兰校核']"]

        # 提交按钮
app_gxrw_fljh_fljh_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
        #工具数量
app_gxrw_fljh_gjsl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[3]/uni-view[2]/uni-view/uni-input/div/input"]
        #扭矩值
app_gxrw_fljh_njz=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[4]/uni-view[2]/uni-view/uni-input/div/input"]
        #平行公差
app_gxrw_fljh_pxgc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view[2]/uni-view/uni-view[2]/uni-view"]
            #平行公差确定
app_gxrw_fljh_pxgc_qd=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[5]/uni-view[2]/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-button[2]"]
        #校核人员
app_gxrw_fljh_jhry=["xpath",""]
        #签名
app_gxrw_fljh_qm=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[9]/uni-view/uni-view"]
            #签名框
app_gxrw_fljh_qm_qmk=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[9]/uni-view/uni-view[2]/uni-view[2]/uni-canvas/div"]
                #签名框保存
app_gxrw_fljh_qm_qmk_bc = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[9]/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-button[2]"]
        #保存
app_gxrw_fljh_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[1]"]
        #提交
app_gxrw_fljh_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
app_gxrw_fljh_=["xpath",""]

    #螺栓抽检
app_gxrw_lscj=["xpath","//uni-view[contains(@class, 'process-item') and text()='螺栓抽检']"]
        #实际施工值
app_gxrw_lscj_sjsgz=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view[2]/uni-view/uni-input/div/input"]
        #保存
app_gxrw_lscj_bc=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[3]/uni-scroll-view/div/div/div/uni-view[1]/uni-view[7]/uni-view[2]/uni-view/uni-input/div/input"]
        #提交
app_gxrw_lscj_tj=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
app_gxrw_lscj_=["xpath",""]
app_gxrw_lscj_=["xpath",""]

        # 提交按钮
app_gxrw_lscj_dpjc_tj = ["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[4]/uni-view[2]"]
app_gxrw_lscj_=["xpath",""]

"""基础数据管理"""
jcsjgl=["xpath","//span[contains(@class, 'el-tooltip__trigger') and text()='基础数据管理']"]
"委托方管理"
jcsjgl_wtfgl=["xpath","//span[contains(@class, 'el-tooltip__trigger') and text()='委托方管理']"]
"服务商管理"
jcsjgl_fwsgl=["xpath","//span[contains(@class, 'el-tooltip__trigger') and text()='服务商管理']"]
 #添加
jcsjgl_fwsgl_tj =["xpath","//span[text()='添加']/parent::button"]
        #添加-服务商名称
jcsjgl_fwsgl_tj_fwsmc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[1]/div/div/div/input"]
        #添加-服务商简称
jcsjgl_fwsgl_tj_fwsjc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[2]/div/div/div/input"]

        #添加-服务商类型
jcsjgl_fwsgl_tj_fwslx =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[3]/div/div/div/div[2]"]

        #添加-服务范围
jcsjgl_fwsgl_tj_fwfw =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[4]/div/div/div/div[1]"]

        #添加-负责人
jcsjgl_fwsgl_tj_fzr =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[5]/div/div/div/input"]

        #添加-联系方式
jcsjgl_fwsgl_tj_lxfs =["xpath",'/html/body/div[1]/div/div/div[4]/div/div/div/div[3]/div/div/div/form/div/div[6]/div/div/div/input']
        #添加—确认
jcsjgl_fwsgl_tj_qd =["xpath","//span[text()='确定']/parent::button"]
        #添加-取消
jcsjgl_fwsgl_tj_qx =["xpath","//span[text()='取消']/parent::button"]
"服务商信息管理"
"设备信息管理"

