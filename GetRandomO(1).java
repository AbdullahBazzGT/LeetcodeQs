class RandomizedSet {
    List<Integer> list;
    Map<Integer, Integer> map;

    public RandomizedSet() {
        this.list = new ArrayList<>();
        this.map = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (map.containsKey(val)) {
            return false;
        }

        list.add(val);
        map.put(val, list.size() - 1); // Map value to its index in the list
        return true;
    }
    
    public boolean remove(int val) {
        if (!map.containsKey(val)) {
            return false;
        }

        // Get the index of the value to be removed
        int index = map.get(val);
        int lastElement = list.get(list.size() - 1);

        // Swap the value to be removed with the last element
        list.set(index, lastElement);
        map.put(lastElement, index);

        // Remove the last element
        list.remove(list.size() - 1);
        map.remove(val);

        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return list.get(rand.nextInt(list.size()))
    }
}
