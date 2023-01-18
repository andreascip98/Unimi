public class C{
	public void c(Object o){ 
		System.out.print("c() -> "); 
		if(o instanceof B) 
			((B)o).b(new A());

		else if(o instanceof A)
			((A)o).a();
	}
}
