package main

import (
	"fmt"
	"path/filepath"

	"github.com/hashicorp/raft-boltdb"
)

func main() {
	logStore, err := raftboltdb.NewBoltStore(filepath.Join("./", "raft.db"))
	if err != nil {
		fmt.Errorf("new bolt store: %s", err)
	}

	fmt.Println(logStore)
}
