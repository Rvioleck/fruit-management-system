use fmdb --Fruits management database
go

create table employee		--Ա����
(
	Eno char(4) not null primary key,          --Ա�����
	Epno char(4),                              --Ա��������
	Ename nvarchar(10) not null,               --Ա������
	Esex nvarchar(2) not null,                 --Ա���Ա�
	Eage int not null,                         --Ա������
	Esalary int not null,                      --Ա��н��
	Eposition nvarchar(10) not null            --Ա��ְ��
)
alter table employee add constraint fk_employee foreign key(Epno) references employee(Eno)
alter table employee add constraint ck1_employee check(Eno like '[0-9][0-9][0-9][0-9]')
alter table employee add constraint ck2_employee check(Epno like '[0-9][0-9][0-9][0-9]')
alter table employee add constraint ck3_employee check(Esex like '��'or Esex like 'Ů')
alter table employee add constraint ck4_employee check(Eposition like 'Ա��'or Eposition like '����')

create table fruit		--ˮ����
(
	Fno char(4) not null primary key,  --ˮ�����
	Fname nvarchar(20) not null unique, --ˮ������
	Fmanu nvarchar(10) not null,        --����
	Fnote nvarchar(40),                 --��ע
	Purchase_price int,                --�����۸�
	Sell_price int,                    --���ۼ۸�
	Storage int,                       --����
	Innumber int,			           --�ۼ��������
	Outnumber int				       --�ۼƳ�������
)
alter table fruit add constraint ck1_fruit check(Fno like '[0-9][0-9][0-9][0-9]')

create table client			--�ͻ���¼��
(
	Cno char(4) not null primary key,       --�ͻ����
	Cname nvarchar(10) not null,				--�ͻ�����	
	Cphone char(11) not null                --�ͻ��绰
)
alter table client add constraint ck1_client check(Cno like '[0-9][0-9][0-9][0-9]')
alter table client add constraint ck2_client check(Cphone like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]')

create table trade_record   --���׼�¼��
(
	Cno char(4) not null primary key check(Cno like '[0-9][0-9][0-9][0-9]'),   --�ͻ����
	Cbuy_time datetime not null,								               --����ˮ����ʱ��
	Cbuy_details nvarchar(100) not null                                         --����ˮ��������
)
alter table trade_record add constraint fk_tr1 foreign key(Cno) references Client(Cno)

