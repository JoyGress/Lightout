#include<iostream>
#include<time.h>
#include<string>

using namespace std;

string get_time(){
	time_t t;
	struct tm ttm;
	t = time(nullptr);
	ttm=*localtime(&t);
	string hour = to_string(ttm.tm_hour);
	string min = to_string(ttm.tm_min);
	string unix_time = hour+":"+min;
	return unix_time;
}

int main(){
	string x = get_time();
	cout<<x<<endl;
	return 0;
}
