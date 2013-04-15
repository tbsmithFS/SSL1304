<div id="bodyBand">

    <div class="staticContentRow">

<h3>List of <?php echo $data['type'] ?></h3>

<?php foreach ($data['listings'] as $listing) { ?>

    <div class="utilityListing">


        <div class="UL_name">
        Name: <?php echo $listing['name'] ?>
        </div>
        <div class="UL_rating">
        Rating: <?php echo $listing['rating'] ?>
        </div>
        <div class="UL_location">
        Location: <?php echo $listing['location'] ?>
        </div>
        <div class="UL_comments">
        Comments: <?php echo $listing['comments'] ?>
        </div>


    </div> <!-- staticContentRow -->

<?php } ?>

</div> <!-- bodyBand -->


