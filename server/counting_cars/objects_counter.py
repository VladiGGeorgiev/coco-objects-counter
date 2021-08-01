
class CarsObjectsCounter:
    def count_cars(self, json_content):
        CAR_CATEGORY_ID = 3
        car_annotations = list(filter(lambda c: c['category_id'] == CAR_CATEGORY_ID, json_content['annotations']))

        center_images_count = 0
        for ann in car_annotations:
            image_dim = self.__get_image_dimentions(ann['image_id'], json_content['images'])
            if self.is_object_in_the_center(image_dim, ann['bbox'], 0.5):
                center_images_count += 1

        return center_images_count

    def is_object_in_the_center(self, image_dim, object_box, match_percentage):
        central_area_box = [image_dim[0] / 4, image_dim[1] / 4, image_dim[0] / 2, image_dim[1] / 2]
        
        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(central_area_box[0], object_box[0])
        yA = max(central_area_box[1], object_box[1])
        xB = min(central_area_box[0] + central_area_box[2], object_box[0] + object_box[2])    
        yB = min(central_area_box[1] + central_area_box[3], object_box[1] + object_box[3])

        # compute the area of intersection rectangle
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
        objectArea = object_box[2] * object_box[3]
        percentage = interArea / objectArea

        return percentage > match_percentage

    def __get_image_dimentions(self, image_id, images):
        image = list(filter(lambda img: img['id'] == image_id, images))[0]
        return (image['width'], image['height'])

    def __download_images(image_ids):
        for id in image_ids:
            image_name = str(id).zfill(12)
            url = f'http://images.cocodataset.org/val2017/{image_name}.jpg'
            response = requests.get(url)

            file = open(f"{image_name}.jpg", "wb")
            file.write(response.content)
            file.close()