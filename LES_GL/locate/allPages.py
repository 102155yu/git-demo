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
xmgl_cypz=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[1]/div[2]/button[1]/span"]
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
xmgl_tssby=["xpath",""]
    #检修范围按钮
xmgl_jxfw=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div/div[1]/div[2]/button[3]/span"]
        #下一页按钮
xmgl_jxfw_xyy=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[4]/button[2]/i"]
        #勾选1
xmgl_jxfw_gx_01=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[1]/div/label/span/span"]
        #提交按钮
xmgl_jxfw_tj=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div[1]/button[1]/span"]
        #提交页面-确认按钮
xmgl_jxfw_tj_qr=["xpath","/html/body/div[7]/div/div/div[3]/button[2]/span"]
    # 角色配置
xmgl_jspz=["xpath",""]
    # 压测
xmgl_yc=["xpath",""]
    #结项
xmgl_jx=["xpath",""]
    # 返回
xmgl_fh=["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/button/span"]
#服务计划管理
fwjh =["xpath","/html/body/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]/div/span"]
    #定力矩服务计划
fwjh_dljfwjh =["xpath","/html/body/div[1]/div/div/div[2]/div/div[1]/div/ul/li[2]/ul/li[2]/span"]
        #添加按钮
fwjh_dljfwjh_tj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[2]/div[1]/button/span"]
            #年月
fwjh_dljfwjh_ny =["xpath",]
            #计划名称
fwjh_dljfwjh_jhmc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[1]/form/div/div[2]/div/div/div/div/input"]
            #检修类型
fwjh_dljfwjh_jxlx =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[1]/form/div/div[3]/div/div/div[1]/div/div[1]/div[2]/span"]
            #计划开始日期
fwjh_dljfwjh_kssj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[1]/form/div/div[4]/div/div/div/div/input"]
            #计划结束日期
fwjh_dljfwjh_jssj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[1]/form/div/div[5]/div/div/div/div/input"]
            #关联进行中计划
fwjh_dljfwjh_gljxzjh =["xpath",]
            #关联历史计划
fwjh_dljfwjh_gllsjh =["xpath",]
            #启用监理
fwjh_dljfwjh_qyjl =["xpath",]
            #监理方
fwjh_dljfwjh_jlf =["xpath",]
            #保存按钮
fwjh_dljfwjh_bc =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[1]/div[2]/button/span"]
            #下派按钮
fwjh_dljfwjh_xp =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[1]/div/div[2]/button[1]/span"]
        # 检修范围配置
            #添加按钮
fwjh_dljfwjh_jxfwpz_tj =["xpath","/html/body/div[1]/div/div/div[4]/div/div/div/div[4]/div[2]/div[1]/div/div/section[2]/div[2]/div/div/button[1]/span"]
                #服务商
fwjh_dljfwjh_jxfwpz_fws =["xpath","/html/body/div[4]/div/div/div/form/div/div[1]/div/div/div/div"]
                #装置
fwjh_dljfwjh_jxfwpz_zz =["xpath","/html/body/div[4]/div/div/div/form/div/div[2]/div/div/div/div"]
                #装置法兰总量
fwjh_dljfwjh_jxfwpz_zzflzl =["xpath",""]
                #计划检修量
fwjh_dljfwjh_jxfwpz_jhjxl =["xpath","/html/body/div[4]/div/div/div/form/div/div[4]/div/div/div[1]/div/input"]
                #服务模式
fwjh_dljfwjh_jxfwpz_fwms =["xpath","/html/body/div[4]/div/div/div/form/div/div[5]/div/div/div/div/div[1]/div[2]/span"]
                #确定按钮
fwjh_dljfwjh_jxfwpz_qd =["xpath","/html/body/div[4]/div/div/footer/button[2]/span"]
                #取消按钮
fwjh_dljfwjh_jxfwpz_qx =["xpath",]
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
'''
    定力矩服务
'''
#工序处理模块
app_dljfw_gxcl_gxcl=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view/uni-view[2]/uni-view[2]/uni-view[1]/uni-image/img"]
    #待领取页签
app_dljfw_gxcl_dlq =["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/div[2]/div[1]/text()"]
    #待处理页签
app_dljfw_gxcl_dql=["xpath",""]
        #勾选框第一个
app_dljfw_gxcl_dql_01=["xpath","/html/body/div[1]/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view[2]/uni-view[2]/uni-scroll-view/div/div/div/uni-view[1]/uni-view/uni-view/uni-view[1]/uni-image/img"]

