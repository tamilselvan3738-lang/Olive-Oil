import shutil
import os

gift_images_list = [
    ('gift_collections.png', 'custom_box.png'),
    ('home_bestseller_box.png', 'holiday_gift1.png'),
    ('home_bestseller_box.png', 'holiday_gift2.png'),
    ('home_bestseller_box.png', 'holiday_gift3.png'),
    ('home_bestseller_box.png', 'holiday_gift4.png'),
    ('gift_collections.png', 'corporate_gifts.png'),
    ('pairing_mediterranean.png', 'bundle_truffle.png'),
    ('pairing_orchard.png', 'bundle_citrus.png'),
    ('bal_giftset.png', 'bundle_balsamic.png'),
    ('chefs_corner.png', 'bundle_chef.png'),
    ('oil_club_box.png', 'pack_ribbon.png'),
    ('oil_club_box.png', 'pack_engrave.png'),
    ('oil_club_box.png', 'pack_note.png')
]

def do_copy_list(mapping_list):
    for src, dst in mapping_list:
        src_path = os.path.join('images', src)
        dst_path = os.path.join('images', dst)
        
        # If source doesn't exist, fallback
        if not os.path.exists(src_path):
            src_path = os.path.join('images', 'home_hero.png')
            
        try:
            shutil.copy(src_path, dst_path)
            print(f"Copied {src_path} -> {dst_path}")
        except Exception as e:
            print(f"Error copying {src} to {dst}: {e}")

print("Copying Gift Box placeholders (fixed)...")
do_copy_list(gift_images_list)
