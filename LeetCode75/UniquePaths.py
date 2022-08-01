class Solution(object):
    def uniquePaths(self, m, n): # O(m*n) 공간복잡도
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n==1:
            return 1
        
        dp = [[0]* n for _ in range(m)]
        
        for i in range(1,m):
            dp[i][0] = 1
        
        for j in range(1,n):
            dp[0][j] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

    def uniquePaths(self, m, n): #O(n) 공간복잡도
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m or not n:
            return 0
        
        cur = [1] * n
        """
        xrange : range와 비슷하다. 그러나 xrange()안의 값이 커지더라도 xrange()의 공간은 그대로인데
        이는 range()의 결과 타입이 list인데 반해, xrange()는 자신에 속한 값을 한번에 로드하지 않고
        , 해당 값에 접근할때마다 값을 하나씩 로드하기 때문이다. 결과 타입도 xrange타입이다
        range()에 비하여 메모리 효율적이지만단, list에 사용할 수 있는 메서드들은 사용하지 못한다
        """
        
        for i in xrange(1,m): 
            for j in xrange(1,n):
                cur[j] += cur[j-1] 
        
        """
        m*n 의 dp배열을 자세히 보면, 대각선 위 와 대각선 밑을 더한다, 
        이는 일차원 배열에서 바로 이전 값(대각선 밑) 와 자기 자신(대각선 위)을 더하는 것과 같다
        따라서 일차원 배열을 여러번 더해가며 처리 가능하다
        """
        
        return cur[-1]
    