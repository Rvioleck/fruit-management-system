use fmdb --Fruits management database
go

create table employee		--员工表
(
	Eno char(4) not null primary key,          --员工编号
	Epno char(4),                              --员工经理编号
	Ename nvarchar(10) not null,               --员工姓名
	Esex nvarchar(2) not null,                 --员工性别
	Eage int not null,                         --员工年龄
	Esalary int not null,                      --员工薪资
	Eposition nvarchar(10) not null            --员工职务
)
alter table employee add constraint fk_employee foreign key(Epno) references employee(Eno)
alter table employee add constraint ck1_employee check(Eno like '[0-9][0-9][0-9][0-9]')
alter table employee add constraint ck2_employee check(Epno like '[0-9][0-9][0-9][0-9]')
alter table employee add constraint ck3_employee check(Esex like '男'or Esex like '女')
alter table employee add constraint ck4_employee check(Eposition like '员工'or Eposition like '经理')

create table fruit		--水果表
(
	Fno char(4) not null primary key,  --水果编号
	Fname nvarchar(20) not null unique, --水果名称
	Fmanu nvarchar(10) not null,        --产地
	Fnote nvarchar(40),                 --备注
	Purchase_price int,                --进货价格
	Sell_price int,                    --出售价格
	Storage int,                       --存量
	Innumber int,			           --累计入库数量
	Outnumber int				       --累计出库数量
)
alter table fruit add constraint ck1_fruit check(Fno like '[0-9][0-9][0-9][0-9]')

create table client			--客户记录表
(
	Cno char(4) not null primary key,       --客户编号
	Cname nvarchar(10) not null,				--客户名字	
	Cphone char(11) not null                --客户电话
)
alter table client add constraint ck1_client check(Cno like '[0-9][0-9][0-9][0-9]')
alter table client add constraint ck2_client check(Cphone like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')

create table trade_record   --交易记录表
(
	Cno char(4) not null primary key check(Cno like '[0-9][0-9][0-9][0-9]'),   --客户编号
	Cbuy_time datetime not null,								               --购买水果的时间
	Cbuy_details nvarchar(100) not null                                         --购买水果的详情
)
alter table trade_record add constraint fk_tr1 foreign key(Cno) references Client(Cno)

