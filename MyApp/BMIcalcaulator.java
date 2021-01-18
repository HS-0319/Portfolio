import java.util.Scanner;
public class BMIcalcaulator {

	public static void main(String[] args) {
		 Scanner scan =new Scanner(System.in);
		 
		 
		 System.out.print("키 : ");
		 double height=scan.nextDouble() / 100;
		 
		 System.out.print("몸무게 : ");
		 double weight=scan.nextDouble();
		 
		 double bmi=weight / (height * height);
		 
		 System.out.print("체질량지수 : ");

		   if(bmi < 18.5)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"저체중입니다.");
		   
		   else if(bmi <23)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"정상입니다.");
			   
		   else if(bmi <25)
			   System.out.println(Math.round(bmi*100.0)/100.0+"," +"과체중입니다.");

		   else if(bmi <30)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"비만입니다.");

		   else
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"고도비만입니다.");

		   



	}

}
