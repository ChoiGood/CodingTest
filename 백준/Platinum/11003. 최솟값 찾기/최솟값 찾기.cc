#include <iostream>
#include <vector>
#include <deque>

using namespace std;

typedef pair<int, int> Node;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, L;
    cin >> N >> L;

    // 슬라이딩 윈도우로 정렬 효과 주기.
    deque<Node> myqueue;
    for (int i = 1; i <= N; i++) {
        int now;
        cin >> now;

        while (myqueue.size() && myqueue.back().second > now) {
            myqueue.pop_back();
        }
        myqueue.push_back(make_pair(i, now));

        if (myqueue.front().first <= i - L) {
            myqueue.pop_front();
        }

        cout << myqueue.front().second << " ";
    }

    return 0;
}