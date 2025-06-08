# LabVIEW Optimal Gear Selection System

## Project Overview

This project determines the optimal gear for maximum torque output based on real-time vehicle speed data. The system interfaces with an OBD2 reader via ELM327 to obtain current vehicle speed and calculates which gear provides the most torque at that specific speed.

## System Architecture

```
shifter.vi (Main VI)
├── shift_points.vi
    ├── intersect.vi
    └── car_config.vi
```

## SubVI Descriptions

### shifter.vi (Main VI)
**Purpose:** Main interface that communicates with OBD2 reader and orchestrates the gear selection process.

**Functionality:**
- Establishes ELM327 Serial VISA connection to OBD2 reader
- Retrieves current vehicle speed in real-time
- Identifies and displays recommended gear to user

**Screenshot:**
![shifter_block](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/shifter_block.png)

![shifter_front](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/shifter_front.png)

### shift_points.vi
**Purpose:** Core calculation engine that determines optimal gear based on torque curves.

**Functionality:**
- Retrieves vehicle configuration from car_config.vi
- Uses intersect.vi to determine gear transition points

**Screenshot:**
![shift_points](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/shift_points_block.png)

### car_config.vi
**Purpose:** Configuration interface for vehicle-specific parameters.

**Functionality:**
- Input interface for gear ratios, and final drive ratio
- Torque curve data entry (RPM vs. Torque values)
- Tire specifications (diameter, circumference, sidewall height)
- Calculates torque output for each gear at any given speed

**Screenshot:**
![car_config_block](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/car_config_block.png)
![car_config_front](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/car_config_front.png)

### intersect.vi
**Purpose:** Mathematical utility for determining line intersections in torque curves.

**Functionality:**
- Calculates intersection points between two lines defined by 4 coordinates
- Validates if intersection occurs within the specified coordinate ranges
- Used to determine gear shift points where torque curves cross
- Returns boolean intersection status and intersection coordinates
- When no intersection occurs between two gear curves, returns maximum possible speed delivered by gear

**Screenshot:**
![intersect](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/intersect_block.png)

## Mathematical and Physical Principles

### Torque-Speed Relationship

The system is based on the fundamental relationship between engine torque, gear ratios, and wheel speed:

$Wheel Torque = Engine Torque \ \times \ Gear Ratio \ \times \ Final Drive Ratio$

$Vehicle Speed = \frac{Engine RPM \ \times \ Tyre Circumference \ \times \ 60}{63360} \div (Gear Ratio \ \times \ Final Drive Ratio)$

*60: converts Engine Revs per minute into Revs per hour*

*63360: number  of inches in a mile*

### Optimal Gear Selection Algorithm

The system operates on the principle that the optimal gear is the one that can deliver the greatest torque at the veehicle's current speed:

1. Calculate torque at the wheels against wheel speed for all gears
2. Identify intersection points for each gear, this is the speed at which the deliverable toque by a gear becomes less than another gear
3. When no intersection exits, a gear is more optimal than any higher gear right up to the engine's maximum RPM (Hit the Redline)
4. Using values from the ODB2 reader, find the vehicle's current speed and then find the gear able to deliver the maximum torque at that gear

This graph, showing the torque against wheel speed for my 2011 Renault Clio, highlights the optimal shift points as calculated by this system. 

![gearedTorqueMPH](https://raw.githubusercontent.com/WllDxn/Gearshift-Indicator/refs/heads/master/img/gearedTorqeMPH.png)
### Line Intersection

The intersect.vi SubVI uses the standard line intersection formula:

For two lines defined by points $(x_{1},y_{1}),(x_{2},y_{2})$ and $(x_{3},y_{3}),(x_{4},y_{4})$:

**Intersection Point:**

$x =\frac{(x_{1}~y_{2}-y_{1}x_{2})(x_{3}-x_{4}) - (x_{1}-x_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4}) - (y_{1}-y_{2})(x_{3}-x_{4})}$

$y = \frac{(x_{1}y_{2}-y_{1}x_{2})(y_{3}-y_{4}) - (y_{1}-y_{2})(x_{3}y_{4}-y_{3}x_{4})}{(x_{1}-x_{2})(y_{3}-y_{4}) - (y_{1}-y_{2})(x_{3}-x_{4})}$
