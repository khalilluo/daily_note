就是用来处理相关事务责任的一条执行链，执行链上有多个节点，每个节点都有机会（条件匹配）处理请求事务，如果某个节点处理完了就可以根据实际业务需求传递给下一个节点继续处理或者返回处理完毕

[![qjpzUs.gif](https://s1.ax1x.com/2022/04/06/qjpzUs.gif)](https://imgtu.com/i/qjpzUs)



```cpp
#ifndef __CHAIN_OF_RESPONSIBILITY_PATTERN_H__
#define __CHAIN_OF_RESPONSIBILITY_PATTERN_H__

#include <mutex>
#include <time.h>
using namespace std;

// 请求：票据
class Bill
{
public:
	Bill(){}
	Bill(int iId, string iName, double iAccount){
		id = iId;
		name = iName;
		account = iAccount;
	}
	double getAccount(){
		return this->account;
	}
	void print(){
		printf("\nID:\t%d\n", id);
		printf("Name:\t%s\n", name.c_str());
		printf("Account:\t%f\n", account);
	}
private:
	int id;
	string name;
	double account;
};

// 抽象处理者
class Approver
{
public:
	Approver(){}
	Approver(string iName){
		setName(iName);
	}
	virtual ~Approver(){}
	// 添加上级
	void setSuperior(Approver *iSuperior){
		this->superior = iSuperior;
	}
	// 处理请求
	virtual void handleRequest(Bill*) = 0;
	string getName(){
		return name;
	}
	void setName(string iName){
		name = iName;
	}
protected:
	Approver *superior;
private:
	string name;
};

// 具体处理者：组长
class GroupLeader :public Approver
{
public:
	GroupLeader(){}
	GroupLeader(string iName){
		setName(iName);
	}
	// 处理请求
	void handleRequest(Bill *bill){
		if (bill->getAccount() < 10){
			printf("组长 %s 处理了该票据，票据信息：",this->getName().c_str());
			bill->print();
		}
		else{
			printf("组长无权处理，转交上级……\n");
			this->superior->handleRequest(bill);
		}
	}
};

// 具体处理者：主管
class Head :public Approver
{
public:
	Head(){}
	Head(string iName){
		setName(iName);
	}
	// 处理请求
	void handleRequest(Bill *bill){
		if (bill->getAccount() >= 10 && bill->getAccount()<30){
			printf("主管 %s 处理了该票据，票据信息：", this->getName().c_str());
			bill->print();
		}
		else{
			printf("主管无权处理，转交上级……\n");
			this->superior->handleRequest(bill);
		}
	}
};

// 具体处理者：经理
class Manager :public Approver
{
public:
	Manager(){}
	Manager(string iName){
		setName(iName);
	}
	// 处理请求
	void handleRequest(Bill *bill){
		if (bill->getAccount() >= 30 && bill->getAccount()<60){
			printf("经理 %s 处理了该票据，票据信息：", this->getName().c_str());
			bill->print();
		}
		else{
			printf("经理无权处理，转交上级……\n");
			this->superior->handleRequest(bill);
		}
	}
};

// 具体处理者：老板
class Boss :public Approver
{
public:
	Boss(){}
	Boss(string iName){
		setName(iName);
	}
	// 处理请求
	void handleRequest(Bill *bill){
		printf("老板 %s 处理了该票据，票据信息：", this->getName().c_str());
		bill->print();
	}
};

#endif //__CHAIN_OF_RESPONSIBILITY_PATTERN_H__
```

```c++
#include <iostream>
#include "ChainOfResponsibility.h"

int main()
{
	// 请求处理者：组长，兵哥，春总，老板
	Approver *zuzhang, *bingge, *chunzong, *laoban;

	zuzhang = new GroupLeader("孙大哥");
	bingge = new Head("兵哥");
	chunzong = new Manager("春总");
	laoban = new Boss("张老板");

    // 此处返回下一个节点可以直接连接多个节点。java常见
    // zuzhang->setSuperior(new Head("兵哥").setSuperior(new Manager("春总").setSuperior(new Boss("张老板"))))
    
	zuzhang->setSuperior(bingge);
	bingge->setSuperior(chunzong);
	chunzong->setSuperior(laoban);

	// 创建报销单
	Bill *bill1 = new Bill(1, "Jungle", 8); 
	Bill *bill2 = new Bill(2, "Lucy", 14.4);
	Bill *bill3 = new Bill(3, "Jack", 32.9);
	Bill *bill4 = new Bill(4, "Tom", 89);

	// 全部先交给组长审批
	zuzhang->handleRequest(bill1); printf("\n");
	zuzhang->handleRequest(bill2); printf("\n");
	zuzhang->handleRequest(bill3); printf("\n");
	zuzhang->handleRequest(bill4);

	printf("\n\n");

	delete zuzhang;
	delete bingge;
	delete chunzong;
	delete laoban;
	delete bill1;
	delete bill2;
	delete bill3;
	delete bill4;

	system("pause");
	return 0;
}
```

