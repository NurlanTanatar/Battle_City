B
    !��^  �            
   @   s  d dl Z d dlmZ dZdZdZdZdZdZd	Z	d	Z
d
Zg ZdZd	Zx:ee�D ].Ze�g � xee�D ]Zee �d � qfW qNW ded d
< e ��  ddgZe j�e�Ze j�d� dZd Ze j�� ZdZ�x.e�s�e j� � Z!�x>e j"�#� D �].Z"e"j$e j%k�rdZe"j$e j&kr�de!d   k�r,dk�rbn n2de!d    k�rLdk�rbn ndZdZe'd� ndZdZde!d   k�r�dk�r�n n2de!d    k�r�dk�r�n ndZdZe'd� ndZdZe!d  e	e  Ze!d e
e  Zy dee e< e'de!dee� W q�   e'de!� Y q�X q�W e�(e� e j)�*eed � e j)�*eed!� x�ee�D ]�Zx�ee�D ]xZeZ+y`ee e �r�edk�r�eZ+nedk�r�eZ+e j)�*ee+ee	 e e ee
 e e e	e
g� W n   Y nX �qbW �qTW e�,d"� e j�-�  q�W e �.�  dS )#�    N)�add)r   r   r   )��   r   r   )r   r   r   )r   r   r   )��   �N   �\   )��   ��   �   �   �   �   �   i�  ix  zArray Backed GridFT�P   �   il  i  )��   �b   r   zclicked brick)��   r   r	   i�  i�  �   zclicked wood)��   r   r	   zClick zGrid coordinates: )i  r   �d   �2   )i�  r   r   r   �<   )/ZpygameZnumpyr   ZBLACKZWHITEZGREENZREDZBRICKZWOODZWIDTHZHEIGHTZMARGINZgridZgrid_wZgrid_h�range�row�append�columnZinitZWINDOW_SIZEZdisplayZset_modeZscreenZset_captionZdoneZ
brushStateZtimeZClockZclockZclickedZmouseZget_pos�posZevent�get�typeZQUITZMOUSEBUTTONDOWN�printZfillZdrawZrectZcolorZtickZflip�quit� r!   r!   �.\lvlcreator.py�<module>   s�   



@
@




