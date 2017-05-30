package Tree;

import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode(int x) { val = x; }
}

public class Solution {
	
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        preOrder(root, res, 0);
        return res;
    }
    public void preOrder(TreeNode root, List<Integer> res, int d) {
    	if(root == null)
    		return ;
    	if(res.size() == d)
    		res.add(root.val);
    	else
    	{
    		res.set(d, Math.max(res.get(d),root.val));
    	}
    	preOrder(root.left, res, d + 1);
    	preOrder(root.right, res, d + 1);
    	
    }

	public static void main(String[] args) {
		//135##3##2#9##
		TreeNode root = new TreeNode(0);
		init(root);
		print(root);
		List<Integer> res = new Solution().largestValues(root);
		for(Integer num : res) {
			System.out.println(num);
		}
	}
	//先序生成树
    public static TreeNode init(TreeNode root) {
    	try {
			char c = (char) System.in.read();
	    	if(c == '#') {
	    		root = null;
	    	}
	    	else {
	    		root.val = Integer.parseInt(String.valueOf(c));
	    		root.left = new TreeNode(55);
	    		root.right = new TreeNode(66);
	    		root.left = init(root.left);
	    		root.right =  init(root.right);
	    	}
	    	return root;
		} catch (IOException e) {
			
			e.printStackTrace();
		}
		return root;
    }
    //中序遍历输出书的结构
    public static void print(TreeNode root) {
    	if(root != null) {
    		print(root.left);
    		System.out.println(root.val);
    		print(root.right);
    	}
    }

}
