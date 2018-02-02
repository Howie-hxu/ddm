# 一般来说，有新的费用类型，就增加“费用类型”
# 有新的部品部门，就增加“项目编号”
# 有新的预算来源，就增加“预算来源”
# 需要注意，如果某个“费用类型”的名字并不是实际统计的，那么需要加到“费用类型别名”
#    例如：研发支出-资本化支出-其他，在生成报表的时候是“研发支出-资本化支出-租赁费”

from collections import OrderedDict
#预算来源 
source_value1="2018  虚拟发薪-先行研究中心  薪资福利支出-EHR预算管控"
source_value2="2018  电机上海研发中心-先行研究中心  研发支出-资本化支出-其他"

budgetSource=dict()
budgetSource["研发支出-资本化支出-工资-绩效"]=source_value1
budgetSource["研发支出-资本化支出-工资-基本工资"]=source_value1
budgetSource["研发支出-资本化支出-工资-其他"]=source_value1
budgetSource["研发支出-资本化支出-职工福利费-人力资源类"]=source_value1
budgetSource["研发支出-资本化支出-社会保险费-医疗保险费"]=source_value1
budgetSource["研发支出-资本化支出-社会保险费-基本养老保险费"]=source_value1
budgetSource["研发支出-资本化支出-社会保险费-失业保险费"]=source_value1
budgetSource["研发支出-资本化支出-社会保险费-工伤保险费"]=source_value1
budgetSource["研发支出-资本化支出-社会保险费-生育保险费"]=source_value1
budgetSource["研发支出-资本化支出-住房公积金"]=source_value1
budgetSource["研发支出-资本化支出-其他"]=source_value2

#费用类型
selectType=set()
selectType.add("研发支出-资本化支出-工资-绩效")
selectType.add("研发支出-资本化支出-工资-基本工资")
selectType.add("研发支出-资本化支出-工资-其他")
selectType.add("研发支出-资本化支出-职工福利费-人力资源类")
selectType.add("研发支出-资本化支出-社会保险费-医疗保险费")
selectType.add("研发支出-资本化支出-社会保险费-基本养老保险费")
selectType.add("研发支出-资本化支出-社会保险费-失业保险费")
selectType.add("研发支出-资本化支出-社会保险费-工伤保险费")
selectType.add("研发支出-资本化支出-社会保险费-生育保险费")
selectType.add("研发支出-资本化支出-住房公积金")
selectType.add("研发支出-资本化支出-其他")

##费用类型别名
alianName=dict()
alianName["研发支出-资本化支出-其他"]="研发支出-资本化支出-租赁费"

#项目编号
item2code=dict()
item2code["伺服电机"]="BPD02016172"
item2code["伺服驱动器"]="BPC00016018"
item2code["M0新平台"]="BRP00016005"
item2code["低成本空调电机"]="BRA00016002"
item2code["高频电感"]="BRP00016004"
item2code["振动噪声专项"]="BTP00016006"
item2code["汽车电子泵"]="BRP00017004"
item2code["皮带减速洗衣机电机驱动器"]="BRP00016003"
item2code["皮带减速洗衣机电机"]="BRA00016007"
item2code["大容量DDM电机"]="BPR00016070"
item2code["滚筒DD电机"]="BRB00016005"
item2code["滚筒DD电机驱动器"]="BRP00016003"
item2code["吸尘器用高速风机"]="BRA00017002"
item2code["自启动永磁电机"]="BRA00016003"
item2code["滚筒洗衣机智能感知"]="BRA00016008"
item2code["DDM驱动器"]="BRA00016009"
item2code["高速破壁机CIM电机及驱动器"]="BPC00016018"
item2code["集成加热洗碗机泵"]="BPD01016129"
item2code["高速破壁机CIM电机及驱动器"]="BPC00016018"
item2code["智能化驱动单元"]="BRP00016010"
item2code["变极变压双转子电机"]="BRP00016008"
item2code["高效、低噪空调压缩机电机"]="BPC00016018"
item2code["80移动空调/除湿机电机竞争力提升"]="BPD02017421"
item2code["RP4极室内机电机竞争力提升"]="BPD02017428"
item2code["春花吸尘器高速电机驱动器"]="BPD02017138"
item2code["春花吸尘器高速电机"]="BPD02017138"
item2code["电机参数实时在线辨识先行研究"]="BRB00017010"
item2code["滚筒BLDC电机噪音改善先行技术研"]="BRA00017008"
item2code["基于M0芯片的滚筒BLDC电机电控平台"]="BRP00017007"
item2code["主动式洗涤"]="BRA00017006"
item2code["zongbu"]="BPC00016018"

#输出的表列
output = OrderedDict([("预算来源",list()),("预算树",list()),("费用类型",list()),("产品线",list()),("借/贷类型",list()),("手工科目组合",list()),("手工科目组合名称",list()),("公司段编码",list()),("成本中心段编码",list()),("会计科目段编码",list()),("明细段/区域段编码",list()),("产品段编码",list()),("内部往来段编码",list()),("备注段编码",list()),("公司段名称",list()),("成本中心段名称",list()),("会计科目段名称",list()),("明细段/区域段名称",list()),("内部往来段名称",list()),("备注段名称",list()),("金额",list()),("本位币金额",list()),("批准金额",list()),("币种",list()),("汇率",list()),("费用发生日期",list()),("AR事务处理类型",list()),("导ERP方式",list()),("摘要",list()),("项目号",list()),("事业部名称",list()),("businessCode",list()),("主体",list())]
)
