public class Visibilidad {
	public static void main(String[] args) {
		Modificadores mf = new Modificadores();
		System.out.println(mf.getData());
		System.out.println(mf.getNumber());
		
		mf.setData("adios");
		mf.setNumber(0);
		
		System.out.println(mf.getData());
		System.out.println(mf.getNumber());
		
		
	}
}
