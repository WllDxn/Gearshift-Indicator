import sys
from datetime import datetime

def setup_logging():
    """Set up logging to a file with timestamp"""
    log_filename = f"line_intersection.log"
    log_file = open(log_filename, 'a')
    return log_file

def log_operation(log_file, message):
    """Log a message to file and print to console"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    # log_file.write(log_entry)


def find_intersection(p1, p2, p3, p4, log_file):
    """
    Find the intersection point of two lines defined by points (p1, p2) and (p3, p4).
    Returns the intersection point or None if lines are parallel or coincident.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)
    if (x1-1 <= x <= x2+1 or x2-1 <= x <= x1+1) and (y1-1 <= y <= y2+1 or y2-1 <= y <= y1+1) and (x3-1 <= x <= x4+1 or x4-1 <= x <= x3+1) and (y3-1 <= y <= y4+1 or y4-1 <= y <= y3+1):
        print(f"{x:.4f}, {y:.4f}")
    else:
        sys.exit(1)
    

    logstring = f"({x1:.4f}, {y1:.4f}) to ({x2:.4f}, {y2:.4f}) Lin: ({x3:.4f}, {y3:.4f}) to ({x4:.4f}, {y4:.4f})"


    if denom == 0:  # Lines are parallel or coincident
        log_operation(log_file, logstring+"- no intersection")
        sys.exit(1)
        return None
    
    # Calculate the numerator for the first line's parameter

    # Calculate the intersection point
    print(((y1 + ua)*(y2 - y1)))
    if (x1-1 <= x <= x2+1 or x2-1 <= x <= x1+1) and (y1-1 <= y <= y2+1 or y2-1 <= y <= y1+1) and (x3-1 <= x <= x4+1 or x4-1 <= x <= x3+1) and (y3-1 <= y <= y4+1 or y4-1 <= y <= y3+1):
        print(f"{x:.4f}, {y:.4f}")
        log_operation(log_file, logstring + f"- intersection at: ({x:.4f}, {y:.4f})")
    else:
        log_operation(log_file, logstring + f"- intersection at: ({x:.4f}, {y:.4f}) - out of bounds")
        sys.exit(1)

def main():
    log_file = setup_logging()
    
    try:
        if len(sys.argv) != 9:
            error_msg = "Error: Expected 8 arguments (4 points as x,y coordinates)"
            log_operation(log_file, error_msg)
            log_operation(log_file, "Usage: python line_intersection.py x1 y1 x2 y2 x3 y3 x4 y4")
            log_operation(log_file, "Where (x1,y1)-(x2,y2) defines the first line and (x3,y3)-(x4,y4) defines the second line")
            sys.exit(1)
        
        # Parse command line arguments
        args = [float(arg) for arg in sys.argv[1:9]]
        x1, y1, x2, y2, x3, y3, x4, y4 = args
        
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)
        p4 = (x4, y4)
        
        find_intersection(p1, p2, p3, p4, log_file)

            
    except ValueError as e:
        error_msg = f"Invalid input: {str(e)} - All arguments must be numbers"
        log_operation(log_file, error_msg)
        sys.exit(1)
    finally:
        log_file.close()

if __name__ == "__main__":
    main()