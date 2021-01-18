public class AuthApp {
 
    public static void main(String[] args) {
         
        
        String[][] users = {
                {"Alpha", "1111"},
                {"Beta", "2222"},
                {"Gamma", "3333"}
        };
        String inputId = args[0];
        String inputPass = args[1];
         
        boolean isLogined = false;
        for(int i=0; i<users.length; i++) {
            String[] current = users[i];
            if(
                    current[0].equals(inputId) && 
                    current[1].equals(inputPass)
            ) {
                isLogined = true;
                break;
            }
        }
        if(isLogined) {
            System.out.println("WELCOME!");
        } else {
            System.out.println("ACCESS DENIED");
        }
 
    }
 
}
