import java.util.*;
import java.io.*;

public class anonymize {

	public static void main (String args[]) throws IOException {
		if (args.length != 4) {
			System.out.println("usage: java anonymize <user_business_rating_csv> <user_b_rating_anonymized_filename> <user_anonymized_filename> <business_anonymized_filename>");
		return;
		}
		

		BufferedReader br = new BufferedReader (new FileReader(args[0]));
		Map<String,Integer> users = new HashMap<String,Integer>();
		Map<String,Integer> businesses = new HashMap<String,Integer>();

		// skip header
		br.readLine();

		String str;
		List<String> tuple = new ArrayList<String>();
		int ucount = 1, bcount = 1;

		while ((str = br.readLine()) != null) {
			String[] t = str.split(",");
			if (!users.containsKey(t[0])) {
				users.put(t[0],ucount++);
			}
			if (!businesses.containsKey(t[1])) {
				businesses.put(t[1],bcount++);
			}
			tuple.add(users.get(t[0])+","+businesses.get(t[1])+","+t[2]);
		}
		writeAllLines(args[1],tuple);
		tuple.clear();

		for (String s : users.keySet()) {
			tuple.add(s+","+users.get(s));
		}

		writeAllLines(args[2],tuple);
		tuple.clear();

		for (String s : businesses.keySet()) {
			tuple.add(s+","+businesses.get(s));
		}

		writeAllLines(args[3],tuple);
		System.out.println("done");
	}

	public static void writeAllLines(String path, List<String>data) throws FileNotFoundException, UnsupportedEncodingException {
		PrintWriter writer = new PrintWriter(path,"UTF-8");
		for (int i = 0; i < data.size(); i++) {
			writer.println(data.get(i));
		}
		writer.close();
	}

}
