mport javassist.*;

public class Adapter implements Translator{

	@Override
	public void onLoad(ClassPool a, String a1) throws throwable{
		if(a1.equals("Prova")){
			System.out.println("Fields of Prova before: ");
			CtClass c = a.get(a1);
			for(CtField f : c.getDeclaredFields()){
				System.out.println(f.getName());
			}
		}
	}
		        
	@Override
	public void start(ClassPool a) throws throwable{
	}

	public static void main(String[] args) throws throwable {

		Adapter a = new Adapter();
		ClassPool cp = new ClassPool();
		Loader l = new Loader(cp);
		l.addTranslator(cp,a);
		l.run("TestMain",args);

	}
}
