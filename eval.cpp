#include <vector>
#include <iostream>
using namespace std;

int countBalancingElements(vector<int>& arr) {
    int count = 0;

    for (int i = 0; i < arr.size(); ++i) {
        int removedElement = arr[i];
        arr.erase(arr.begin() + i);
        int evenSum = 0, oddSum = 0;
        for (int j = 0; j < arr.size(); j=+2) {
                evenSum += arr[j];
                if(j+1<arr.size()){
                oddSum += arr[j+1];
                }
           }
        // Check if deleting the current element makes the sums equal
        if (evenSum == oddSum) {
            ++count;
        }

        // Restore the array to its original state
        arr.insert(arr.begin() + i, removedElement);
    }

    return count;
}

int main() {
    vector<int> arr = {5,5,2,5,8};
    cout << "Number of balancing elements: " << countBalancingElements(arr) << endl;
    return 0;
}