#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Student
{
    public:
    int scores[5]; //5 điểm của 1 học sinh
    void input(){
        for (int i = 0; i < 5; i++){
            cin >> scores[i]; // nhập điểm của 1 học sinh
        }
    }
    int calculateTotalScore(){
        int count = 0;
        for (int i = 0; i < 5; i++){
            count += scores[i]; // tổng điểm của học sinh đó
        }
    return count; // trả về tổng điểm
    }
};

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    Student st[1000]; // khai báo biến
    int n;
    cin >> n; // nhập số học sinh
    for (int i = 0; i < n; i++){
        st[i].input(); //nhập điểm của n học sinh
    }
    int Kritens_grades = st[0].calculateTotalScore(); // điểm của Kristen mặc định là hàng thứ 0
    int count = 0; // biến đếm số học sinh có điểm lớn hơn Kristen
    for (int i = 1; i < n; i++){
        int others_grades = st[i].calculateTotalScore(); // tổng điếm (tính từ học sinh thứ 2 (hàng thứ 1))
        if (others_grades > Kritens_grades){
            count ++;
        } 
    }
    cout << count;
    return 0;
}
