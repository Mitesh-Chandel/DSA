public class best_time_to_buy_and_sell_stock {
    class Solution {
    public int maxProfit(int[] prices) {
        int profit =0;
       int minprice = prices[0];
       for( int i=0;i < prices.length;i++){
         if(prices[i]<minprice){
            minprice=prices[i];
         }
         int currentpro = prices[i]-minprice ;
         if(currentpro>profit){
            profit=currentpro ;
         }
       }
        return profit ;  
    }
}
    
}
