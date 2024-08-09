#include <cstdio>
#include <cstring>

bool alp[26];

int main() {
	int N = 20;
	char S[55], alp[3];
	double time, sum = 0.0, cnt = 0.0;

	while (N--) {
		scanf("%s %lf %s", S, &time, alp);
		if (alp[0] != 'P') {
			if (alp[0] != 'F')
				sum += time * (('E' - alp[0]) + 0.5 * (alp[1] == '+'));
			cnt += time;
		}
	}
	printf("%lf", sum / cnt);
}