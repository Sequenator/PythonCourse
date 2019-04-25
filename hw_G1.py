def saver(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        
        with open(func.__name__ + '.txt', 'a') as f:
            f.write(str(return_value) + '\n')
            
        return return_value
        
    return wrapper
    

@saver
def tf():
    a = 'Hello, World!'
    return(a)
    
    
def main():
    print(tf())

if __name__ == '__main__':
    main()
