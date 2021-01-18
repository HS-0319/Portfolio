import java.util.Scanner;
public class gugudan {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		
		int input;
		while(true){
			System.out.println("2에서 9까지 숫자 중 하나 입력하세요.");
			input = scan.nextInt();
			if(input >= 2 && input <= 9) break;
			System.out.println("숫자를 다시 입력해주세요.");
		}
		
		for(int i = 1; i <= 9; i++) {
			System.out.println(input + "X" + i + "=" + input*i);
			
		}

	}

}
