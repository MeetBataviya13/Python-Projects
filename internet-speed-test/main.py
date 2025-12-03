from tkinter import *
import speedtest
def speedcheck():
    # Create Speedtest object
    st = speedtest.Speedtest()
    
    # Fetch server list for accurate speed test
    st.get_best_server()
    
    # Perform download speed test (in Mbps)
    download_speed = st.download() / (10**6)
    
    # Perform upload speed test (in Mbps)
    upload_speed = st.upload() / (10**6)
    
    # Display results
    lab_down.config(text=f"Download Speed: {download_speed:.2f} Mbps")
    lab_up.config(text=f"Upload Speed: {upload_speed:.2f} Mbps")

# Main programm
sp = Tk() 
sp.title("Internet Speed Test")
sp.geometry("600x400")
sp.config(bg="#2c3e50") 

# Define fonts
title_font = ("Verdana", 28, "bold") 
label_font = ("Arial", 18)
button_font = ("Arial", 18, "bold")

# Title label
Label(sp, text="Internet Speed Test", font=title_font, bg="#2c3e50", fg="#ecf0f1").place(x=30, y=20)

# Download Speed label and result
Label(sp, text="Download Speed", font=label_font, bg="#2c3e50", fg="#ecf0f1").place(x=30, y=90)
lab_down = Label(sp, text="0.00 Mbps", font=label_font, bg="#2c3e50", fg="#ecf0f1")
lab_down.place(x=30, y=130)

# Upload Speed label and result
Label(sp, text="Upload Speed", font=label_font, bg="#2c3e50", fg="#ecf0f1").place(x=30, y=180)
lab_up = Label(sp, text="0.00 Mbps", font=label_font, bg="#2c3e50", fg="#ecf0f1")
lab_up.place(x=30, y=220)

# Check Speed button
Button(sp, text="CHECK SPEED", font=button_font, bg="#3498db", fg="#ecf0f1", relief=RAISED, padx=20, pady=10, command=speedcheck).place(x=30, y=280)

# Exit button
Button(sp, text="EXIT", font=button_font, bg="#e74c3c", fg="#ecf0f1", relief=RAISED, padx=20, pady=10, command=sp.destroy).place(x=270, y=280)

# Footer label
Label(sp, text="Note: This test may take a few moments.", font=("Arial", 12), bg="#2c3e50", fg="#bdc3c7").place(x=30, y=350)

# Start the main loop
sp.mainloop()


