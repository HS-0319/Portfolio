import java.util.Scanner;
public class gugudan {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		
		int input;
		while(true){
			System.out.println("2���� 9���� ���� �� �ϳ� �Է��ϼ���.");
			input = scan.nextInt();
			if(input >= 2 && input <= 9) break;
			System.out.println("���ڸ� �ٽ� �Է����ּ���.");
		}
		
		for(int i = 1; i <= 9; i++) {
			System.out.println(input + "X" + i + "=" + input*i);
			
		}

	}

}
