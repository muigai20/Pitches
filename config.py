import os

class Config:
    """Main configurations class"""
    pass



class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    
    

class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}