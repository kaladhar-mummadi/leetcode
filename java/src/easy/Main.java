package src.easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Stock {
	double quantity;
	double price;
	String name;
	double percentNAV;
	
	public Stock(String name){
	
	}
	public Stock(String name, double quantity, double price) {
		this.quantity = quantity;
		this.price = price;
		this.name = name;
	}
	
	public double getQuantity() {
		return quantity;
	}
	
	public double getPrice() {
		return price;
	}
	
	public String getName() {
		return name;
	}
	
	public void setQuantity(double quantity) {
		this.quantity = quantity;
	}
	
	public void setPrice(double price) {
		this.price = price;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	
	public double getAssetValue(){
		return quantity*price;
	}
	
	public double getPercentNAV() {
		return percentNAV;
	}
	
	public void setPercentNAV(double percentNAV) {
		this.percentNAV = percentNAV;
	}
}

class StockInfo{
	String name;
	Stock Port;
	Stock Bench;
	
	public StockInfo(String name) {
		this.name = name;
		this.setPort(new Stock(name));
		this.setBench(new Stock(name));
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public Stock getPort() {
		return Port;
	}
	
	public void setPort(Stock port) {
		Port = port;
	}
	
	public Stock getBench() {
		return Bench;
	}
	
	public void setBench(Stock bench) {
		Bench = bench;
	}
}
class Portfolio {
	Map<String, StockInfo> stocks;
	
	public Portfolio() {
		stocks = new TreeMap();
	}
	
	public void addStock(StockInfo stock){
		stocks.put(stock.getName(), stock);
	}
	
	public double calculatePortNAV(){
		double totalAssetValue = 0;
		for(StockInfo stock : stocks.values()){
			totalAssetValue+=stock.getPort().getAssetValue();
		}
		return totalAssetValue;
	}
	
	public double calculateBenchNAV(){
		double totalAssetValue = 0;
		for(StockInfo stock : stocks.values()){
			totalAssetValue+=stock.getBench().getAssetValue();
		}
		return totalAssetValue;
	}
	
	public void calculatePortPercentNav(StockInfo s){
		double percentNAV = (s.getPort().getAssetValue()*100)/calculatePortNAV();
		s.getPort().setPercentNAV(percentNAV);
	}
	
	public void calculateBenchPercentNav(StockInfo s){
		double percentNAV = (s.getBench().getAssetValue()*100)/calculateBenchNAV();
		s.getBench().setPercentNAV(percentNAV);
	}
	
	public StockInfo getStock(String name){
		if(stocks.containsKey(name)){
			return stocks.get(name);
		} else {
			return new StockInfo(name);
		}
	}
	
}
public class Main {
	private static Portfolio inventory;
	
	public static void main(String[] args) throws IOException {
		InputStreamReader reader = new InputStreamReader(System.in);
		BufferedReader in = new BufferedReader(reader);
		String line;
		while ((line = in.readLine()) != null) {
			parseInput(line);
			calculateDiffNAV();
		}
	}
	
	public static void calculateDiffNAV(){
		StringBuilder result = new StringBuilder();
		for(StockInfo stock: inventory.stocks.values()){
			inventory.calculatePortPercentNav(stock);
			inventory.calculateBenchPercentNav(stock);
			System.out.printf("%s:%.2f,",stock.getName(),stock.getPort().getPercentNAV()-stock.getBench().getPercentNAV());
		}
		
	}
	
	public static String getWord(String line, Integer index, char delimiter) {
		StringBuilder current = new StringBuilder();
		while (line.charAt(index) != delimiter) {
			current.append(line.charAt(index));
			index++;
		}
		
		return current.toString();
	}
	
	
	public static String getComaValue(String line, int index) {
		StringBuilder current = new StringBuilder();
		while (line.charAt(index) != ',') {
			current.append(line.charAt(index));
		}
		
		return current.toString();
	}
	
	public static void parseInput(String line){
		inventory = new Portfolio();
		//bench = new Portfolio();
		Stock newStock;
		StockInfo newStockInfo;
		int commaCount =0;
		Boolean isPort= true;
		String name="";
		String quantity = "";
		String price = "";
		StringBuilder current = new StringBuilder();
		int i = 0;
		while (i < line.length()) {
			String type  = getWord(line, i, ':');
			name = getWord(line, i, ',');
			quantity = getWord(line, i, ',');
			price = getWord(line, i, '|');
			
			newStock = new Stock(name, Double.parseDouble(quantity), Double.parseDouble(price));
			if (type == "PORT") {
			
			}else {
			
			}
		
		}
		for(char c: line.toCharArray()){
			if(c==':'){
				clear(current);
			} else if(c==','){
				commaCount++;
				switch (commaCount){
					case 1: name = current.toString();
						clear(current);
						break;
					case 2: quantity = current.toString();
						clear(current);
						commaCount = 0;
						break;
				}
				
			} else if(c==';'){
				price = current.toString();
				clear(current);
				
				newStock = new Stock(name, Double.parseDouble(quantity), Double.parseDouble(price));
				if(isPort){
					//port.addStock(newStock);
					newStockInfo = new StockInfo(name);
					newStockInfo.setPort(newStock);
					inventory.addStock(newStockInfo);
					
				} else {
					newStockInfo = inventory.getStock(name);
					newStockInfo.setBench(newStock);
					inventory.addStock(newStockInfo);
				}
			} else if(c=='|'){
				price = current.toString();
				clear(current);
				
				newStock = new Stock(name, Double.parseDouble(quantity), Double.parseDouble(price));
				newStockInfo = new StockInfo(name);
				newStockInfo.setPort(newStock);
				inventory.addStock(newStockInfo);
				isPort = false;
			} else{
				current.append(c);
			}
		}
		price = current.toString();
		clear(current);
		
		newStock = new Stock(name, Double.parseDouble(quantity), Double.parseDouble(price));
		newStockInfo = inventory.getStock(name);
		newStockInfo.setBench(newStock);
		inventory.addStock(newStockInfo);
	}
	
	private static void clear(StringBuilder current){
		current.setLength(0);
	}
}