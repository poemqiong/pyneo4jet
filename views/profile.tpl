<div>{{user.username}}</div>
<div><img src={{user.avatar}} /></div>
% if user.username == owner.username:
<a href="/{{user.username}}/?action=profile">Update Profile</a>
<a href="/{{user.username}}/?action=password">Update Password</a>
% elif isfollow:
<form action="/{{user.username}}/?action=unfollow" method="POST">
    <input type="submit" value='unfollow'/>
</form>
% else:
<form action="/{{user.username}}/?action=follow" method="POST">
    <input type="submit" value='follow'/>
</form>
% end
% for tweet in tweets:
<div>
    <div>{{tweet.username}}</div>
    <div>{{tweet.text}}</div>
    <div>{{tweet.created_at}}</div>
</div>
% end
% rebase base title=user.username, username=user.username
