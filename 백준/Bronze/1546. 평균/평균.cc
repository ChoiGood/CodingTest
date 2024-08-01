#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N; 
    cin >> N;

    vector<float> score_lst;

    for (int i = 0; i < N; i++) {
        float score;
        cin >> score;
        score_lst.push_back(score);
    }

    int M = *max_element(score_lst.begin(), score_lst.end());

    float sum;
    for (int i = 0; i < N; i++) {
        score_lst[i] = (score_lst[i] / M) * 100;
        sum += score_lst[i];
    }

    // for (float score : score_lst) {
    //     cout << score << " ";
    // }
    // cout << "\n";
    cout << sum / N;

    return 0;
}