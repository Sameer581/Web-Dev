def fetch_weather(): 

    city = city_entry.get() 

    if city: 

        api_key = "YOUR_API_KEY"  # Replace with your actual API key 

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 

        try: 

            response = requests.get(url) 

            weather_data = response.json() 

            if weather_data.get('cod') != 200: 

                messagebox.showerror("Error", f"City {city} not found.") 

            else: 

                temp = weather_data['main']['temp'] 

                desc = weather_data['weather'][0]['description'] 

                result_label.config(text=f"Temperature: {temp}°C\nDescription: {desc}") 

        except Exception as e: 

            messagebox.showerror("Error", str(e)) 

    else: 

        messagebox.showwarning("Input Error", "Please enter a city name.") 

 

# Create main window 

root = tk.Tk() 

root.title("Weather App") 

 

# Add widgets 

tk.Label(root, text="Enter city name:").grid(row=0, column=0, padx=10, pady=10) 

city_entry = tk.Entry(root) 

city_entry.grid(row=0, column=1, padx=10, pady=10) 

 

tk.Button(root, text="Fetch Weather", command=fetch_weather).grid(row=1, column=0, columnspan=2, pady=10) 

 

result_label = tk.Label(root, text="") 

result_label.grid(row=2, column=0, columnspan=2, pady=10) 

 

root.mainloop() 