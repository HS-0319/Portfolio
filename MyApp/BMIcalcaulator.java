import java.util.Scanner;
public class BMIcalcaulator {

	public static void main(String[] args) {
		 Scanner scan =new Scanner(System.in);
		 
		 
		 System.out.print("Ű : ");
		 double height=scan.nextDouble() / 100;
		 
		 System.out.print("������ : ");
		 double weight=scan.nextDouble();
		 
		 double bmi=weight / (height * height);
		 
		 System.out.print("ü�������� : ");

		   if(bmi < 18.5)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"��ü���Դϴ�.");
		   
		   else if(bmi <23)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"�����Դϴ�.");
			   
		   else if(bmi <25)
			   System.out.println(Math.round(bmi*100.0)/100.0+"," +"��ü���Դϴ�.");

		   else if(bmi <30)
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"���Դϴ�.");

		   else
			   System.out.println(Math.round(bmi*100.0)/100.0+","+"�����Դϴ�.");

		   



	}

}
