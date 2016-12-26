public class Solution {
	//看到这个题是求二进制代码对应的不同位数时，第一反应就应该是异或 ^ 
    public int hammingDistance(int x, int y) {

    	String s = Integer.toBinaryString(x ^ y);
    	int count = 0;
    	for(int i = 0; i<s.length(); i++)
    	{
    		if(s.charAt(i) == '1')
    			count++;
    	}
    	return count;
    }
}