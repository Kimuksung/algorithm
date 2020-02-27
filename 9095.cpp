#include <iostream>
using namespace std;
#include <vector>
int arr[100];

int answer(int temp2) {
	int answer2;
	vector<int> temp;
	arr[1] = 1;
	arr[2] = 2;
	arr[3] = 4;

	for (int i = 4;i <= temp2;i++) {
		arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
	}
	return arr[temp2];
}

int main() {
	int n;
	cin >> n;
	for (int i = 0;i < n;i++) {
		int temp;
		cin >> temp;

		cout<<answer(temp)<<endl;
	}


	return 0;
}