# flipdigit-demo


![PXL_20250621_110526811](https://github.com/user-attachments/assets/1adea397-6143-4a98-b2e1-d1736bbf51ac)

Demo code for driving the Alfazeta Flipdigit 7-segment display (with RS485 interface board) 
https://flipdots.com/en/products-services/small-7-segment-displays/
I used a cheap USB RS485 adapter from eBay
 
Wiring - my adapter was labelled A and B, the Flipdigit data sheet has +RS and -RS
I wired +RS to A and -RS to B. I also connected USB ground to Flipdigit ground.

![image](https://github.com/user-attachments/assets/974cfec4-dc18-4a02-989f-0a2dcefb5b68)


I ran the Flipdigit from 24V DC.

The vendor's web page says
   At these coil drive parameters, the duty cycle for driving the same segment must be less than 5% (on/off time)
   therefore allow at least 900msec before driving the same segment again. 
   This will ensure that the segment coil will not accumulate heat.
This code pays no attention to this limit. Please do not blame me if you melt your display.
