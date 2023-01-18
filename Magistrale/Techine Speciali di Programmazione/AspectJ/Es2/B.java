public class B{
	public void b(Object o){ 
		System.out.print("b() -> ");
		if(o instanceof C)
			((C)o).c(new A());

		if(o instanceof A)
			((A)o).a();
	} 
}
